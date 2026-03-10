#!/bin/bash
set -e

echo "🔍 Validando conectividade..."
ping -c 3 $(terraform output -raw public_ip)

echo "🧪 Validando API..."
curl -s http://$(terraform output -raw public_ip)/health | grep -q "healthy"

echo "📊 Validando métricas..."
kubectl get pods -n monitoring

echo "✅ Todos os testes passaram!"
