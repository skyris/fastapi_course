import datetime
from typing import List, Optional
from data.package import Package
from data.release import Release

def release_count() -> int:
    return 2_234_847

def package_count() -> int:
    return 274_000

def latest_packages(limit=5) -> List:
    return [
        {'id': 'fastapi', 'summary': "A great web framework"},
        {'id': 'uvicorn', 'summary': "Your favorite ASGI server"},
        {'id': 'httpx', 'summary': "Requests for an async world"},
    ][:limit]

def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        package_name,
        "This is the summary",
        "Full details here!",
        "http://fastapi.tiangolo.com/",
        "MIT",
        "Victor Klimov",
        [
            {
                "name": "Skyris",
                "profile_image_url": "https://avatars.githubusercontent.com/u/10289173?s=40&v=4"
            },
            {
                "name": "Marley",
                "profile_image_url": "https://avatars.githubusercontent.com/u/10372159?s=64&v=4"
            }
        ]
    )
    return package


def get_latest_release(package_name: str) -> Optional[Release]:
    return Release("1.2.0", datetime.datetime.now())
