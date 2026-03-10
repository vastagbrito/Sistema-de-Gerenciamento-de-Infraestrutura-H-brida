import subprocess
import yaml
import os
import sys

class HybridInfrastructure:
    def __init__(self, config_path):
        self.config = self._load_config(config_path)
        
    def _load_config(self, path):
        with open(path) as f:
            return yaml.safe_load(f)
    
    def deploy(self):
        print("🚀 Iniciando deploy híbrido...")
        
        # 1. Terraform
        print("🔧 Provisionando recursos...")
        subprocess.run(["terraform", "init"], check=True)
        subprocess.run(["terraform", "apply", "-auto-approve"], check=True)
        
        # 2. Ansible
        print("🔄 Configurando servidores...")
        subprocess.run(["ansible-playbook", "ansible/playbooks/deploy.yml"], check=True)
        
        # 3. Kubernetes
        print("🐳 Aplicando configurações K8s...")
        subprocess.run(["kubectl", "apply", "-f", "kubernetes/"], check=True)
        
        # 4. Docker
        print("📦 Buildando imagens Docker...")
        subprocess.run(["docker", "build", "-t", "app:latest", "."], check=True)
        
        # 5. Validação
        print("✅ Validando deploy...")
        subprocess.run(["./scripts/validate.sh"], check=True)
        
        print("✅ Deploy completo!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: ./main.py <config.yaml>")
        sys.exit(1)
        
    manager = HybridInfrastructure(sys.argv[1])
    manager.deploy()
