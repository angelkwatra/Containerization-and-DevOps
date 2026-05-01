# EXPERIMENT 12 – KUBERNETES: DEPLOYMENT & ORCHESTRATION

This document outlines the steps performed during Experiment 12, which focuses on learning Kubernetes for container orchestration, scaling, and self-healing.

## Concept Overview
**Kubernetes (K8s)** is an industry-standard open-source system for automating deployment, scaling, and management of containerized applications.

### Key Features vs Docker Swarm
| Feature | Swarm | Kubernetes |
| :--- | :--- | :--- |
| **Setup** | Easy | Complex |
| **Scaling** | Basic | Advanced |
| **Ecosystem** | Small | Huge |
| **Industry use** | Rare | Standard |

### Core Concepts
* **Pod**: The smallest deployable computing unit, consisting of one or more containers. Pods are temporary.
* **Deployment**: Defines how the application runs (replicas, image, etc.) and ensures the desired number of pods are always running.
* **Service**: Provides stable network access and load balancing to expose your application to users, abstracting away the dynamic IP addresses of Pods.
* **ReplicaSet**: Ensured by the Deployment to maintain the required number of running pods for self-healing.

---

### Step 1: Create a Deployment for WordPress
We start by creating a Deployment to ensure that 2 replicas of the WordPress container are running.

1. Apply the deployment configuration:
```bash
kubectl apply -f wordpress-deployment.yaml
```

**Screenshot 1:** Terminal showing the successful `deployment.apps/wordpress created` message.
![Screenshot 1](./screenshots/1.png)

---

### Step 2: Create a Service to Expose WordPress
To access WordPress from outside the cluster, we create a NodePort service.

1. Apply the service configuration:
```bash
kubectl apply -f wordpress-service.yaml
```

**Screenshot 2:** Terminal showing the successful `service/wordpress-service created` message.
![Screenshot 2](./screenshots/2.png)

---

### Step 3: Verify Setup and Run Services
We verify that the Pods are running and the Service is correctly exposing ports.

1. Check the running pods and services:
```bash
kubectl get pods
kubectl get svc
```

**Screenshot 3:** Terminal showing the 2 running WordPress pods.
![Screenshot 3](./screenshots/3.png)

**Screenshot 4:** Terminal showing the `wordpress-service` with its NodePort (30007).
![Screenshot 4](./screenshots/4.png)

---

### Step 4: Access the Application
Since we are using local clusters, we use port-forwarding to access the NodePort on our localhost.

1. Forward the port and access the site in the browser:
```bash
kubectl port-forward service/wordpress-service 30007:80
```
Navigate to `http://localhost:30007` to see the WordPress installation UI.

**Screenshot 5:** Browser showing the WordPress setup screen.
![Screenshot 5](./screenshots/5.png)

---

### Step 5: Scale the Application
We scale the number of WordPress replicas to 4 to demonstrate load distribution.

1. Run the scale command and verify:
```bash
kubectl scale deployment wordpress --replicas=4
kubectl get pods
```

**Screenshot 6:** Terminal showing 4 WordPress pods running (scaling up).
![Screenshot 6](./screenshots/6.png)

---

### Step 6: Test Self-Healing
Kubernetes automatically replaces failed pods. Let's test this by deleting one.

1. Delete one of the running pods and immediately check the pods again:
```bash
kubectl delete pod <pod-name>
kubectl get pods
```
*Kubernetes notices the missing pod, and the ReplicaSet spins up a new replacement pod instantly.*

**Screenshot 7:** Terminal showing the pod being deleted.
![Screenshot 7](./screenshots/7.png)

**Screenshot 8:** Terminal showing the new pod being automatically created to maintain the desired replica count of 4.
![Screenshot 8](./screenshots/8.png)

