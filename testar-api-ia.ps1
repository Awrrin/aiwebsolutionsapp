Write-Host "IA Web Solutions - Testador de API via PowerShell" -ForegroundColor Cyan

# Perguntar o prompt
$prompt = Read-Host "Digite seu prompt para a IA"

# Perguntar o token do webhook
$token = Read-Host "Digite seu token de segurança (WEBHOOK_SECRET do .env)"

# Montar o JSON
#$json = @{ prompt = $prompt } | ConvertTo-Json -Compress
$json = "{`"prompt`": `"$prompt`"}"


# Configurar os headers
$headers = @{
  "Content-Type"    = "application/json"
  "x-webhook-token" = $token
}

# Fazer requisição POST
$response = Invoke-RestMethod -Uri "http://localhost:8000/falar" `
  -Method POST `
  -Headers $headers `
  -Body $json

# Mostrar resultado
Write-Host ""
Write-Host "RESPOSTA DA IA:" -ForegroundColor Green
Write-Host $response.resposta -ForegroundColor Yellow
