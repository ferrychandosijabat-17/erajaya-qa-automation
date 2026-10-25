# Enforce TLS 1.2 for modern HTTPS connections in Windows PowerShell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 -bor [Net.SecurityProtocolType]::Tls11 -bor [Net.SecurityProtocolType]::Tls

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

$headers = @{
    "Content-Type" = "application/json"
    "Accept"       = "application/json"
}

$userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

foreach ($u in $users) {
    $index++
    $body = @{
        userName = $u.username
        password = $u.password
    } | ConvertTo-Json

    try {
        $response = Invoke-RestMethod -Uri $url -Method Post -Body $body -Headers $headers -UserAgent $userAgent -TimeoutSec 15
        Write-Host "[$index/$total] [SUCCESS] Terdaftar: $($u.username) (UserID: $($response.userID))" -ForegroundColor Green
        $successCount++
    }
    catch {
        $errText = ""
        # Di Windows PowerShell, body error disimpan di ErrorDetails.Message
        if ($_.ErrorDetails -and $_.ErrorDetails.Message) {
            $errText = $_.ErrorDetails.Message
        }
        elseif ($_.Exception.Response) {
            try {
                $stream = $_.Exception.Response.GetResponseStream()
                if ($stream) {
                    $reader = New-Object System.IO.StreamReader($stream)
                    $errText = $reader.ReadToEnd()
                }
            } catch {
                $errText = $_.Exception.Message
            }
        }

        if (-not $errText) {
            $errText = $_.Exception.Message
        }
        
        # DemoQA mengembalikan 406 Not Acceptable jika user sudah ada (User exists!)
        if ($errText -like "*User exists*" -or $errText -like "*1204*" -or "$($_.Exception.Message)" -like "*406*") {
            Write-Host "[$index/$total] [INFO] User sudah terdaftar: $($u.username)" -ForegroundColor Yellow
            $successCount++
        }
        else {
            Write-Host "[$index/$total] [FAIL] Gagal mendaftarkan: $($u.username) - $errText" -ForegroundColor Red
        }
    }

    Start-Sleep -Milliseconds 250
}

Write-Host "`nSelesai: $successCount dari $total user siap digunakan!" -ForegroundColor Cyan
