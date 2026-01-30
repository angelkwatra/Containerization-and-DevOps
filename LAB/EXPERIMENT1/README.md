# EXPERIMENT 1  
## Comparison of Virtual Machines (VMs) and Containers using Ubuntu and Nginx  

**Note:** Instead of VAGRANT, Multipass (by Canonical – Ubuntu) is used (suitable for modern ARM systems).  

It provides:  
- Automated VM creation  
- Automated VM deletion  
- No ISO handling  
- CLI-driven  
- Scriptable  
- Perfect for labs  

---

## Experiment Setup – Automated VM using Multipass (macOS ARM)

### Step 1: Install Multipass
```bash
brew install multipass
```
![Install Multipass](lab1image1.png)

---

### Step 2: Create Ubuntu VM (Automated)
```bash
multipass launch jammy --name vm-lab1
```
![Create VM](lab1image2.png)

---

### Step 3: Access the VM
```bash
multipass shell vm-lab1
```
![Access VM](lab1image3.png)

---

### Step 4: Install Nginx inside VM
```bash
sudo apt update
sudo apt install -y nginx
sudo systemctl start nginx
```
![Install Nginx](lab1image4.png)

---

### Step 5: Verify Nginx
```bash
curl localhost
```
![Verify Nginx](lab1image5.png)

---

### Performance Analysis (VM – Activity Monitor)
![CPU Load VM](CPULOADVM.png)  
![Memory Usage VM](MEMORYUSAGEVM.png)  
![Network Performance VM](NETWORKPERFORMANCEVM.png)  
![Packets VM](PACKETS.png)  

---

### Step 6: Delete the VM
```bash
multipass delete vm-lab1
multipass purge
```
![Delete VM](lab1image6.png)

---

## Running Ubuntu Environment using Docker (macOS)

### Step 1: Verify Docker
```bash
docker --version
```

---

### Step 2: Verify Available Ubuntu Images
```bash
docker images
```

---

### Step 3: Create and Start Ubuntu Container
```bash
docker run -it --name ubuntu-vm ubuntu:22.04 /bin/bash
```
![Run Container](lab1image7.png)

---

### Step 4: Update Package List and Install Nginx and Curl
```bash
apt update
apt install -y nginx curl
service nginx start
```
![Install in Container](lab1image8.png)

---

### Step 5: Verify Nginx in Container
```bash
curl localhost
```
![Verify Container Nginx](lab1image9.png)

---

### Performance Analysis (Container – Activity Monitor)
![Container Performance 1](cont1.png)  
![Container Performance 2](cont2.png)  
![Container Performance 3](cont3.png)  
![Container Performance 4](cont4.png)  
![Container Performance 5](cont5.png)  

---

## Conclusion  
This experiment demonstrates the difference between running an Ubuntu environment using a Virtual Machine (Multipass) and a Docker container.  
Containers are lightweight and faster compared to Virtual Machines, which require a full OS and consume more system resources.
