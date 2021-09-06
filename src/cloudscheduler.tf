resource "google_cloud_scheduler_job" "yfinance" {
  name        = var.project
  schedule    = "0 0 * * *"

  pubsub_target {
    # topic.id is the topic's full resource name.
    topic_name = google_pubsub_topic.yfinance.id
    data       = base64encode("trigger_me")
  }
}
