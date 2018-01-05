---
layout: default
title: MFC project enhancements
---

## {{ page.title }}
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
4. to change the fonts of differnt text (rather than change all of them), use the `SetFont` in `WMInitDialog`
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
5. to set the focus on the password edit bar (so that the user can start entering password without having to select it), add the following:
```
GetDlgItem(IDC_EDIT1)->SetFocus();
```
and we have to change the return value of `OnInitDialog()` to `FALSE`, as `MSDN` explains
>If OnInitDialog returns nonzero, Windows sets the input focus to the first control in the dialog box.
>
>The application can return 0 only if it has explicitly set the input focus to one of the controls in the dialog box.


* **
<span style="font-family:Arial">
GDI（图形设备接口）
PDC (设备环境对象)
GDI的派生类有：CBitmap, CBrush, CFont....
上述`4`中的例子， `f`是CFont这个类创建的一个动态对象，在MFC中，无需显式的delete这些动态对象。
C++中，类的定义放在.h文件中，而.cpp文件存放类外定义的成员函数
</span>
