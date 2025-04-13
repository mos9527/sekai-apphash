com.sega.pjsekai (5.2.0, jp)
---
Reported Package: com.sega.pjsekai

|                                        app_hash|   app_region|  app_version|   ab_version|
|------------------------------------------------|-------------|-------------|-------------|
|            4ca841be-5890-6c8e-930d-eb172f8993c3|           jp|        5.2.0|        5.2.0|

- CLI Usage:

        sssekai abcache --app-platform android --app-region jp --app-version 5.2.0 --app-appHash 4ca841be-5890-6c8e-930d-eb172f8993c3 --app-abVersion 5.2.0

- Python Usage:

        from sssekai.abcache import AbCacheConfig

        AbCacheConfig(
            app_region="jp",
            app_version="5.2.0",
            ab_version="5.2.0",
            app_hash="4ca841be-5890-6c8e-930d-eb172f8993c3",
            app_platform="android"
        )

