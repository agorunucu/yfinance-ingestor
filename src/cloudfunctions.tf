data "archive_file" "function_code" {
  type = "zip"
  source_dir = "${path.module}/codebase/ingestor"
  output_path = "${path.module}/codebase/ingestor.zip"
}

resource "google_storage_bucket_object" "function_code" {
  # It will trigger function codebase refresh when the function code is updated.
  name = "codebase/cloudfunctions/ingestor-${data.archive_file.function_code.output_md5}.zip"
  bucket = var.default_bucket
  source = data.archive_file.function_code.output_path
}

resource "google_cloudfunctions_function" "function" {
  name = "${var.project}-ingestor"
  runtime = "python39"
  entry_point = "main"

  timeout = 540  # max
  available_memory_mb = 1024
  source_archive_bucket = google_storage_bucket_object.function_code.bucket
  source_archive_object = google_storage_bucket_object.function_code.name
  event_trigger {
    event_type = "google.pubsub.topic.publish"
    resource = google_pubsub_topic.yfinance.name
  }
  environment_variables = {
    # Secrets should be stored in the Secrets Manager.
    # But the current permissions does not permit to retrieve secret data.
    # So, these resources are not used at the moment.
    # I will not delete them for the possible future improvements.
    # "SECRET_SNOWFLAKE_ACCOUNT" = google_secret_manager_secret.snowflake_account.id
    # "SECRET_SNOWFLAKE_USER" = google_secret_manager_secret.snowflake_user.id
    # "SECRET_SNOWFLAKE_PASSWORD" = google_secret_manager_secret.snowflake_password.id
    # "SECRET_SNOWFLAKE_DATABASE" = google_secret_manager_secret.snowflake_database.id
    # "SECRET_SNOWFLAKE_SCHEMA" = google_secret_manager_secret.snowflake_schema.id
    "SNOWFLAKE_ACCOUNT" = var.snowflake_account
    "SNOWFLAKE_USER" = var.snowflake_user
    "SNOWFLAKE_PASSWORD" = var.snowflake_password
    "SNOWFLAKE_DATABASE" = var.snowflake_database
    "SNOWFLAKE_SCHEMA" = var.snowflake_schema
  }
}

# IAM entry for all users to invoke the function
resource "google_cloudfunctions_function_iam_member" "invoker" {
  project = var.project_id
  region = var.region
  cloud_function = google_cloudfunctions_function.function.name

  role = "roles/cloudfunctions.invoker"
  member = "allUsers"
}
