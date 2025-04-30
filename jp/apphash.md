com.sega.pjsekai (5.3.0, jp)
---
Reported Package: com.sega.pjsekai

|                                        app_hash|   app_region|  app_version|   ab_version|
|------------------------------------------------|-------------|-------------|-------------|
|            2a9bb18f-c309-1993-5b6e-9f25ddc88be3|           jp|        5.3.0|        5.3.0|

- CLI Usage:

        sssekai abcache --app-platform android --app-region jp --app-version 5.3.0 --app-appHash 2a9bb18f-c309-1993-5b6e-9f25ddc88be3 --app-abVersion 5.3.0

- Python Usage:

        from sssekai.abcache import AbCacheConfig

        AbCacheConfig(
            app_region="jp",
            app_version="5.3.0",
            ab_version="5.3.0",
            app_hash="2a9bb18f-c309-1993-5b6e-9f25ddc88be3",
            app_platform="android"
        )

