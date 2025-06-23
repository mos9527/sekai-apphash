com.sega.pjsekai (5.4.0, jp)
---
Reported Package: com.sega.pjsekai

|                                        app_hash|   app_region|  app_version|   ab_version|
|------------------------------------------------|-------------|-------------|-------------|
|            9c046d6d-3f06-6370-d932-7a43220d83ad|           jp|        5.4.0|        5.4.0|

- CLI Usage:

        sssekai abcache --app-platform android --app-region jp --app-version 5.4.0 --app-appHash 9c046d6d-3f06-6370-d932-7a43220d83ad --app-abVersion 5.4.0

- Python Usage:

        from sssekai.abcache import AbCacheConfig

        AbCacheConfig(
            app_region="jp",
            app_version="5.4.0",
            ab_version="5.4.0",
            app_hash="9c046d6d-3f06-6370-d932-7a43220d83ad",
            app_platform="android"
        )

