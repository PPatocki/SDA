provider "google" {
    project = "civil-lightning-237716"
    zone = "europe-west3-c"
    credentials = "/home/cray/SDA/terraform/account.json"
}
resource "google_compute_address" "ip-1" {
    name = "our-instance1-ip"
}


resource "google_compute_network" "vpc-network-1"{
    name = "vpc-network-1"
    auto_create_subnetworks = "true"
    routing_mode = "GLOBAL"
}

resource "google_compute_network" "vpc-network-2"{
    name = "vpc-network-2"
    auto_create_subnetworks = "true"
}

resource "google_compute_firewall" "simple-firewall"{
    name = "simple-firewall"
    network = "${google_compute_network.vpc-network-1.name}"
    allow {
      protocol = "icmp"
    }
    allow {
      protocol = "tcp"
      ports = ["0-65535"]
    }



}
#######################################################################################

resource "google_compute_instance" "our-instance1" {
    "boot_disk" {
        initialize_params {
            size = 30
            image = "ubuntu-1804-lts"
}
}

    machine_type = "g1-small"
    name = "our-instance1"
    "network_interface" {
        network = "${google_compute_network.vpc-network-1.self_link}"
        access_config {
          nat_ip = "${google_compute_address.ip-1.address}"
}
}
}
#######################################################################################

resource "google_compute_instance" "our-instance2" {
    "boot_disk" {
        initialize_params {
            size = 30
            image = "ubuntu-1804-lts"
}           
}           

    machine_type = "g1-small"
    name = "our-instance2"
    "network_interface" {
        network = "${google_compute_network.vpc-network-1.self_link}"
}
}
#######################################################################################
resource "google_compute_instance" "our-instance3" {
    "boot_disk" {
        initialize_params {
            size = 30
            image = "ubuntu-1804-lts"
}           
}           

    machine_type = "g1-small"
    name = "our-instance3"
    zone = "asia-northeast1-a"
    "network_interface" {
        network = "${google_compute_network.vpc-network-2.self_link}"
}
}

