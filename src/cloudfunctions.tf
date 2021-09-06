data "archive_file" "function_code" {
  type = "zip"
  source_dir = "${path.module}/codebase/ingestor"
  output_path = "${path.module}/codebase/ingestor.zip"
}

resource "google_storage_bucket_object" "function_code" {
  name   = "codebase/cloudfunctions/ingestor.zip"
  bucket = var.default_bucket
  source = data.archive_file.function_code.output_path
}

resource "google_cloudfunctions_function" "function" {
  name        = "${var.project}-ingestor"
  runtime     = "python39"

  available_memory_mb   = 128
  source_archive_bucket = google_storage_bucket_object.function_code.bucket
  source_archive_object = google_storage_bucket_object.function_code.name
  event_trigger {
    event_type = "google.pubsub.topic.publish"
    resource = google_pubsub_topic.yfinance.name
  }
}

# IAM entry for all users to invoke the function
resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = google_cloudfunctions_function.function.project
  region         = google_cloudfunctions_function.function.region
  cloud_function = google_cloudfunctions_function.function.name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}
