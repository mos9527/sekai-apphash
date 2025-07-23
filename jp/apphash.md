com.sega.pjsekai (5.5.0, jp)
---
Reported Package: com.sega.pjsekai

|                                        app_hash|   app_region|  app_version|   ab_version|
|------------------------------------------------|-------------|-------------|-------------|
|            7d3ddef6-22d5-eecb-3a7b-77181b2d8eae|           jp|        5.5.0|        5.5.0|

- CLI Usage:

        sssekai abcache --app-platform android --app-region jp --app-version 5.5.0 --app-appHash 7d3ddef6-22d5-eecb-3a7b-77181b2d8eae --app-abVersion 5.5.0

- Python Usage:

        from sssekai.abcache import AbCacheConfig

        AbCacheConfig(
            app_region="jp",
            app_version="5.5.0",
            ab_version="5.5.0",
            app_hash="7d3ddef6-22d5-eecb-3a7b-77181b2d8eae",
            app_platform="android"
        )

