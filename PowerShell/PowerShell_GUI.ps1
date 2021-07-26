# Init PowerShell GUI
Add-Type -AssemblyName System.Windows.Forms

# Create a new form
$NewForm = New-Object System.Windows.Forms.Form
$NewForm.ClientSize = '500,300'
$NewForm.text = "Sample GUI"
$NewForm.BackColor = "#000000"


# Display the form
[void]$NewForm.ShowDialog()