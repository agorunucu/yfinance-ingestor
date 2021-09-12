resource "google_app_engine_application" "app" {
  project     = "bux-bi-assignment-agorunucu"
  location_id = var.region
}
