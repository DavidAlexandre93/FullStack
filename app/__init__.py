"""FastAPI app creation."""

from fastapi import FastAPI
from app.controller.bucket_s3_controller import bucket_router


def create_app():
    tags_metadata = [
        {
            "name": "Bucket S3",
            "description": "Read and Save file Bucket S3",
            "externalDocs": {
                "description": "Items external docs",
                "url": "https://app-send-emails.herokuapp.com/docs",
            },

        },

        {
            "name": "API Bucket S3",
            "description": "Read and Save file Bucket S3 **Cloud & Computing**.",
        },
    ]
    description = """
    API Bucket S3. 🚀

    ## description

    Site **David & Developer**.

    ## Software & Developer

    You will be able to:

    * **Get read_file_bucket_data** (_implemented_).
    * **Post save_file_bucket_data** (_implemented_).
    """
    app = FastAPI(title="BucketS3",
                  description=description,
                  version="0.0.1",
                  terms_of_service="http://example.com/terms/",
                  contact={
                      "name": "David Alexandre Fernandes",
                      "url": "https://www.davidalexandrefernandes.com.br",
                      "email": "davidalexandrefernandes@outlook.com",
                  },
                  license_info={
                      "name": "Apache 2.0",
                      "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
                  },
                  openapi_tags=tags_metadata
                  )

    app.include_router(bucket_router, prefix="/api/v1")

    return app
