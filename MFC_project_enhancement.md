1. when nothing is ordered, the order will not be rocorded.
2. add an option of getting today's bill only in the manager mode.
```
if (substr[0] != today && m_today == TRUE)
		continue;
```
and for the `check` button:
```
m_today = !m_today;
```
3. in the manager mode, redirect the ENTER button to call the function `OnButton1`
```
BOOL CManagerDlg::PreTranslateMessage(MSG* pMsg)
{
	// TODO: Add your specialized code here and/or call the base class
	if (pMsg->message == WM_KEYDOWN)
		if (pMsg->wParam == VK_RETURN)
		{CManagerDlg::OnButton1();
		return true;}
	return CDialog::PreTranslateMessage(pMsg);
}
```
4. to change the font of differnt text, use the `SetFont` in `WMInitDialog`
```
CFont * f;
	f = new CFont;
  f->CreateFont(36, // nHeight   
    0, // nWidth   
    0, // nEscapement   
    0, // nOrientation   
    FW_BOLD, // nWeight   
    TRUE, // bItalic   
    FALSE, // bUnderline   
    0, // cStrikeOut   
    ANSI_CHARSET, // nCharSet   
    OUT_DEFAULT_PRECIS, // nOutPrecision   
    CLIP_DEFAULT_PRECIS, // nClipPrecision   
    DEFAULT_QUALITY, // nQuality   
    DEFAULT_PITCH | FF_SWISS, // nPitchAndFamily   
    _T("Arial")); // lpszFac   
	GetDlgItem(IDC_BUTTON1)->SetFont(f);
```
