from typing import Tuple
import requests, os, sys, logging, argparse
from concurrent.futures import ThreadPoolExecutor
from contextlib import redirect_stdout

QOOAPP_TOKEN = os.environ.get("QOOAPP_TOKEN", None)
assert QOOAPP_TOKEN, "Environment variable QOOAPP_TOKEN not set."


logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger("updater")


class QooApp(requests.Session):
    app_id: int

    def __init__(self, app_int: int):
        super().__init__()
        self.app_id = app_int
        self.headers.update(
            {
                "X-Version-Code": "80608",
                "X-Device-ABIs": "arm64-v8a,armeabi-v7a,x86,x86_64",
                "X-User-Token": QOOAPP_TOKEN,
            }
        )

    def fetch(self) -> Tuple[str, str]:
        """hash, url"""
        resp = self.get(f"https://api.qqaoop.com/store/v11/apps/{self.app_id}")
        resp.raise_for_status()
        resp = resp.json()
        assert resp["code"] == 200, resp
        resp = resp["data"]
        return (
            f'MD5 {resp["apk"]["baseApkMd5"]}',
            f"https://api.ppaooq.com/v11/apps/{resp['packageId']}/download",
        )


class PlainETag(requests.Session):
    url: str

    def __init__(self, url: str):
        super().__init__()
        self.url = url

    def fetch(self, retries=5) -> Tuple[str, str]:
        for _ in range(retries):
            try:
                resp = self.get(self.url, stream=True)
                resp.raise_for_status()
                etag = resp.headers.get("ETag", None)
                assert etag, f"ETag not found for {self.url}"
                return f"ETag {etag}", self.url
            except Exception as e:
                logger.warning(f"failed to fetch {self.url}: {e}")
                if _ == retries - 1:
                    raise e
                logger.warning(f"retrying {self.url}...")


def soruce(region: str) -> requests.Session:  # hash, url
    # fmt: off
    match region:
        case "jp": 
            return QooApp(9038)
        case "en":
            return QooApp(18337)
        case "cn":
            return PlainETag("https://ugapk.com/djogd")        
        case "tw":
            return QooApp(18298)
        case "kr":
            return QooApp(20082)
    # fmt: on


def cmd(*command):
    cmd = " ".join(command)
    logger.info(f"running command: cmd")
    return os.system(cmd)


def fetch(region: str):
    CWD = lambda *a: os.path.abspath(os.path.join(region, *a))
    os.makedirs(CWD(), exist_ok=True)
    try:
        src = soruce(region)
        new_hash, url = src.fetch()
    except Exception as e:
        logger.error(f"failed metadata fetch on {region}: {e}")
        return

    try:
        if os.path.exists(CWD("pacakge_hash")):
            with open(CWD("pacakge_hash"), "r") as f:
                old_hash = f.read().strip()
                if old_hash == new_hash:
                    logger.info(f"hash unchanged on {region}: {old_hash}. skipping.")
                    return
                else:
                    logger.info(f"hash changed on {region}: {old_hash} -> {new_hash}.")
    except Exception as e:
        logger.error(f"failed to update hash file on {region}: {e}")
        return

    try:
        os.makedirs(CWD(".temp"), exist_ok=True)
        headers = [f'"{k}: {v}"' for k, v in src.headers.items()]
        cmd_headers = ["--header"] * len(headers) * 2
        cmd_headers[1::2] = headers
        ret = cmd(
            "aria2c",
            "-x16",
            "-s16",
            "--enable-http-pipelining",
            "--allow-overwrite=true",
            *cmd_headers,
            url,
            "-d",
            CWD(".temp"),
            "-o",
            f"{region}.apk",
        )
        assert ret == 0
    except Exception as e:
        logger.error(f"failed to download {region}: {e}")
        return

    try:
        with open(CWD("pacakge_hash"), "w") as f:
            f.write(new_hash)
            logger.info(f"hash file updated on {region}: {new_hash}.")
    except Exception as e:
        logger.error(f"failed to update hash file on {region}: {e}")
        return


def apphash(region: str):
    CWD = lambda *a: os.path.abspath(os.path.join(region, *a))
    if not os.path.exists(CWD(".temp", f"{region}.apk")):
        logger.error(f"apk not found on {region}.")
        return
    from sssekai.entrypoint.apphash import main_apphash

    class NamedDict(dict):
        def __getattribute__(self, name: str):
            try:
                return super().__getattribute__(name)
            except AttributeError:
                return self.get(name, None)

    with open(CWD("apphash.json"), "w") as f:
        with redirect_stdout(f):
            main_apphash(
                NamedDict(
                    {
                        "apk_src": CWD(".temp", f"{region}.apk"),
                        "format": "json",
                        "deep": True
                    }
                )
            )

    with open(CWD("apphash.md"), "w") as f:
        with redirect_stdout(f):
            main_apphash(
                NamedDict(
                    {
                        "apk_src": CWD(".temp", f"{region}.apk"),
                        "format": "markdown",
                        "deep": True
                    }
                )
            )


def __main__():
    REGIONS = ["jp", "en", "cn", "tw", "kr"]
    parser = argparse.ArgumentParser("Sekai AppHash updater")
    parser.add_argument(
        "-r",
        "--region",
        type=str,
        default="all",
        choices=REGIONS,
        help="region to update",
    )
    parser.add_argument(
        "--skip-download",
        action="store_true",
        help="skip downloading the apk and pull hashes immediately",
    )
    args = parser.parse_args()
    if args.region != "all":
        REGIONS = [args.region]

    if not args.skip_download:
        with ThreadPoolExecutor(max_workers=8) as executor:
            for region in REGIONS:
                executor.submit(fetch, region)

    for region in REGIONS:
        apphash(region)


if __name__ == "__main__":
    __main__()
