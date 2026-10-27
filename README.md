🚀 K8s Architecture: Real-Time eBPF Security & Knative Serverless

Tento projekt predstavuje produkčnú mikroslužbovú architektúru v Kubernetes klastri (kind). Obsahuje kompletný 3-tier stack, real-time zabezpečenie Linuxového jadra pomocou eBPF (Tetragon) a Serverless autoscaling (Knative Serving).



🛠️ Použitý Stack

Orchestrácia: Kubernetes (kind - K8s in Docker)
Backend & Databáza: Python (Flask), Redis DB
eBPF Security: Cilium Tetragon (TracingPolicy)
Serverless / Autoscaling: Knative Serving, Kourier Ingress
Správa balíkov: Helm, kubectl




🎯 Hlavné Funkcionality & Výsledky

1. 3-Tier Architektúra & Internal DNS
Nasadenie backendu a databázy pomocou K8s Deployment a Service objektov.
Prepojenie mikroslužieb pomocou internej K8s DNS služby (redis-db:6379).

2. eBPF Ochrana Kernela v reálnom čase (Tetragon)
Vytvorenie TracingPolicy na monitorovanie systémových volaní sys_execve
Výsledok: Pokus o neautorizovaný vstup do shellu (kubectl exec -it ... -- /bin/sh) bol zablokovaný priamo v Linuxovom jadre s návratovým kódom exit code 137 (SIGKILL).

3. Serverless "Scale-to-Zero" (Knative)
Preklopenie aplikácie na Knative Service (KSVC).
Výsledok: Po 10 sekundách neaktivity sa počet bežiacich podov automaticky zníži na 0 (0 % spotreba CPU/RAM). Pri príchode HTTP požiadavky vykoná Knative okamžitý Cold Start a spracuje požiadavku.





kubectl apply -f k8s/block-shell.yaml

# 3. Nasadenie Serverless Služby (Knative)
kubectl apply -f k8s/serverless-backend.yaml
