$csvPath = Join-Path $PSScriptRoot "..\data\users.csv"
$url = "https://demoqa.com/Account/v1/User"

if (-not (Test-Path $csvPath)) {
    Write-Error "File users.csv tidak ditemukan di $csvPath"
    exit 1
}

Write-Host "Membaca data user dari $csvPath..." -ForegroundColor Cyan
$users = Import-Csv -Path $csvPath

$total = $users.Count
$successCount = 0
$index = 0

foreach ($u in $users) {
    $index++
    $body = @{
        userName = $u.username
        password = $u.password
    } | ConvertTo-Json

    try {
        $response = Invoke-RestMethod -Uri $url -Method Post -Body $body -ContentType "application/json" -TimeoutSec 15
        Write-Host "[$index/$total] [SUCCESS] Terdaftar: $($u.username) (UserID: $($response.userID))" -ForegroundColor Green
        $successCount++
    }
    catch {
        $stream = $_.Exception.Response.GetResponseStream()
        $reader = New-Object System.IO.StreamReader($stream)
        $errText = $reader.ReadToEnd()
        
        if ($errText -like "*User exists*") {
            Write-Host "[$index/$total] [INFO] User sudah terdaftar: $($u.username)" -ForegroundColor Yellow
            $successCount++
        }
        else {
            Write-Host "[$index/$total] [FAIL] Gagal mendaftarkan: $($u.username) - $errText" -ForegroundColor Red
        }
    }

    Start-Sleep -Milliseconds 400
}

Write-Host "`nSelesai: $successCount dari $total user siap digunakan!" -ForegroundColor Cyan
