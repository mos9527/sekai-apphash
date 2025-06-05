com.hermes.mk (4.1.1, cn)
---
Reported Package: com.sega.pjsekai

|                                        app_hash|   app_region|  app_version|   ab_version|
|------------------------------------------------|-------------|-------------|-------------|
|            41fd71f2-f715-bc10-5852-0a9d8542f760|           cn|        4.1.1|        4.1.0|

- CLI Usage:

        sssekai abcache --app-platform android --app-region cn --app-version 4.1.1 --app-appHash 41fd71f2-f715-bc10-5852-0a9d8542f760 --app-abVersion 4.1.0

- Python Usage:

        from sssekai.abcache import AbCacheConfig

        AbCacheConfig(
            app_region="cn",
            app_version="4.1.1",
            ab_version="4.1.0",
            app_hash="41fd71f2-f715-bc10-5852-0a9d8542f760",
            app_platform="android"
        )

