# Experiment 3 -- Deploying NGINX Using Different Base Images and Comparing Image Layers

## Objective

- Deploy NGINX using official image
- Build custom NGINX image using Ubuntu base
- Build custom NGINX image using Alpine base
- Compare image sizes and layers

---

## Environment Used

- Host OS: macOS (Apple Silicon)
- Container Platform: Docker Desktop

---

## Experiment Execution with Screenshots

# 🔹 Part 1 -- Using Official NGINX Image

### Step 1: Pull, Run and Verify NGINX

```bash
docker pull nginx:latest
docker run -d --name nginx-official -p 8080:80 nginx
curl http://localhost:8080
```

![Step 1 -- Pull, Run and Verify NGINX](0.png)

---

### Step 2: Verify Image

```bash
docker images nginx
```

![Step 2 -- Verify Image](1.png)

---

# 🔹 Part 2 -- Build NGINX Using Ubuntu Base

### Step 3: Create Dockerfile (Ubuntu)

```dockerfile
FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

![Step 3 -- Ubuntu Dockerfile](2.png)

---

### Step 4: Build Image

```bash
docker build -t nginx-ubuntu .
```

![Step 4 -- Build Ubuntu Image](3.png)

---

### Step 5: Run Ubuntu-based NGINX

```bash
docker run -d --name nginx-ubuntu -p 8081:80 nginx-ubuntu
```

![Step 5 -- Run Ubuntu NGINX](4.png)

---

### Step 6: Verify Ubuntu Image Size

```bash
docker images nginx-ubuntu
```

![Step 6 -- Ubuntu Image Size](5.png)

---

# 🔹 Part 3 -- Build NGINX Using Alpine Base

### Step 7: Build Alpine Image

```bash
docker build -t nginx-alpine .
```

![Step 7 -- Build Alpine Image](6.png)

---

### Step 8: Run Alpine-based NGINX

```bash
docker run -d --name nginx-alpine -p 8082:80 nginx-alpine
```

![Step 8 -- Run Alpine NGINX](7.png)

---

### Step 9: Verify Alpine Image Size

```bash
docker images nginx-alpine
```

![Step 9 -- Alpine Image Size](8.png)

---

### Step 10: Compare All Image Sizes

```bash
docker images | grep nginx
```

![Step 10 -- Compare Image Sizes](9.png)

---

# 🔹 Part 4 -- Custom NGINX Configuration

### Step 11: Create Custom HTML and NGINX Config

```bash
mkdir html
# Create custom index.html and nginx configuration
docker run -d --name nginx-custom -p 8083:80 -v $(pwd)/html:/usr/share/nginx/html nginx
```

![Step 11 -- Custom NGINX Config](10.png)

---

### Step 12: Run NGINX with Bind Mount

```bash
docker run -d --name nginx-volume -p 8084:80 -v $(pwd)/html:/usr/share/nginx/html nginx
```

![Step 12 -- NGINX with Bind Mount](11.png)

---

## Result

- Official NGINX image deployed successfully
- Custom Ubuntu-based NGINX image created
- Custom Alpine-based NGINX image created
- Compared image sizes and observed Alpine image is significantly smaller
- Custom NGINX configuration deployed using bind mounts
