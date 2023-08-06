"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import storage

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket("my-bucket", location="US")

bucket_object = storage.BucketObject(
    "index.html", bucket=bucket.name, source=pulumi.FileAsset("assets/index.html")
)

bucket_iam_binding = storage.BucketIAMBinding(
    "my-bucket-binding",
    bucket=bucket.name,
    role="roles/storage.objectViewer",
    members=["allUsers"],
)
# Export the DNS name of the bucket
pulumi.export("bucket_name", bucket.url)
