# B22CS022_VCC_ASGN01
VirtualBox Microservices with RabbitMQ

Overview

This repository contains the necessary files to set up and deploy a microservice-based application using VirtualBox. It includes scripts for configuring Virtual Machines (VMs), setting up RabbitMQ as a message broker, and implementing a producer-consumer architecture using Python.

Project Structure

📂 Virtualbox-Microservices
│-- 📄 README.md (Project documentation)
│-- 📄 LICENSE (License information)
│-- 📄 .gitignore (Ignored files)
│-- 📄 producer.py (Producer script)
│-- 📄 consumer.py (Consumer script)

Installation & Setup

1. Install VirtualBox

For Linux Users

sudo apt update
sudo apt install -y virtualbox

For Windows Users

Download VirtualBox from the official website: VirtualBox and follow the installation instructions.

2. Create and Configure VMs

Follow the steps in the project documentation to create and configure three Virtual Machines:

VM1: RabbitMQ Broker

VM2: Producer

VM3: Consumer

3. Install Dependencies

Run the following command on VM2 and VM3:

sudo apt install -y python3-pip
pip install pika

4. Running the Application

--Start RabbitMQ Broker on VM1

sudo systemctl start rabbitmq-server

--Run Consumer on VM3

python3 consumer.py

--Run Producer on VM2

python3 producer.py

Author

Gubbala Bhargavi

