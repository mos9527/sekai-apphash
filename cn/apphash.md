com.hermes.mk (3.4.1, cn)
---
Reported Package: com.sega.pjsekai

|                                        app_hash|   app_region|  app_version|   ab_version|
|------------------------------------------------|-------------|-------------|-------------|
|            a3015fe8-785f-27e1-fb8b-546a23c82c1f|           cn|        3.4.1|        3.4.0|

- CLI Usage:

        sssekai abcache --app-platform android --app-region cn --app-version 3.4.1 --app-appHash a3015fe8-785f-27e1-fb8b-546a23c82c1f --app-abVersion 3.4.0

- Python Usage:

        from sssekai.abcache import AbCacheConfig

        AbCacheConfig(
            app_region="cn",
            app_version="3.4.1",
            ab_version="3.4.0",
            app_hash="a3015fe8-785f-27e1-fb8b-546a23c82c1f",
            app_platform="android"
        )

