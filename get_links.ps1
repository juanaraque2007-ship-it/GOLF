$html = Invoke-RestMethod -Uri 'https://www.fedgolfclm.com/informacion-fgclm-ley-de-transparencia/'
$regex = '(?i)<a\s+[^>]*href=["'']([^"''\s]+\.pdf)["''][^>]*>(.*?)</a>'
$matches = [regex]::Matches($html, $regex, 'IgnoreCase,Singleline')

foreach ($match in $matches) {
    $text = $match.Groups[2].Value -replace '(?s)<[^>]+>', ''
    $text = $text.Trim()
    $href = $match.Groups[1].Value
    Write-Output "$text -> $href"
}
