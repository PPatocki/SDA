provider "google" {
    project = "civil-lightning-237716"
    zone = "europe-west3-c"
    credentials = "/home/cray/SDA/terraform/account.json"
}
resource "google_compute_address" "our-address" {
    name = "our-address"
}

resource "google_compute_instance" "our-instance" {
    "boot_disk" {
        initialize_params {
            size = 30
            image = "ubuntu-1804-lts"
}
}
    machine_type = "g1-small"
    name = "our-instance"
    "network_interface" {
        network = "default"
        access_config {
          nat_ip = "${google_compute_address.our-address.address}"
}
}
}
