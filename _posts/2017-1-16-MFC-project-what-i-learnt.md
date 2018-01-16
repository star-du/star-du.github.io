---
layout: post
title: MFC project:what I have learnt
teaser: It's part of our assignment to finish a MFC program as the final project for Software-tech-basis. This really really old and outdated app is hard to use for nowadays, but it may offer some insights into the C language.
category: coding
tags: [C, reviews]
---
It's part of our assignment to finish a MFC program as the final project for Software-tech-basis. This really really old and outdated app is hard to use for nowadays, but it may offer some insights into the C language.
##  basic notions
GDI（图形设备接口)	\\
PDC (设备环境对象) \\
GDI的派生类有：CBitmap, CBrush, CFont....


上述`4`中的例子， `f`是CFont这个类创建的一个动态对象，在MFC中，无需显式的delete这些动态对象。

C++中，类的定义放在.h文件中，而.cpp文件存放类外定义的成员函数
下面`6`中的方法可以更改某个控件的属性		

读取csv的方法：		

```file.Open(_T("../main./order.csv"),CFile::modeRead);
CString str;
while(file.ReadString(str))
	{CString substr[10];
	int count=0;
	int index = str.Find(_T(","));
	CString stmp;
	while (index != -1 && count<9)
	{
	substr[count++] = str.Left(index);
	str=str.Right(str.GetLength()-index-1);
	index = str.Find(_T(","));
	}
	substr[count++]=str;
	}
	file.Close();
```
以上会在每个外层while循环内部，将各个单元格（此处不超过10个）的内容以字符串的形式储存在substr数组的各个元素中，在实际应用中，需要对字符串再做处理（如使用`atoi()`函数将字符串转化为整数）。

* **
## our enhancements of the program
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

6. change the color of text:
1.add declaration of m_brush `CBrush m_brush` in Dlg.h
2.
~~~if(pWnd->GetDlgCtrlID()==IDC_EDIT1)//如果是编辑框
    {   pDC->SetTextColor(RGB(255,0,0));//设置编辑框字体的颜色
        pDC->SetBkColor(RGB(255,255,0));//设置字体背景颜色
        CFont font;
        font.CreatePointFont(100,"华文楷体");
         pDC->SelectObject(&font);//设置字体        
        return m_brush;}
~~~
we do so because MFC hints that  
`Return a different brush if the default is not desired`
7. everytime when opening each sub_dialog, the `OnInitDialog` function would show the current order status of each dish.
To do this, just edit the m_password (a string which is the variable for the IDC_EDIT1), and then `UpdateData(FALSE)`
8. for the background picture, add the following code into `onpaint()`:
```
    CPaintDC   dc(this);     
    CRect   rect;
    GetClientRect(&rect);//get the length and the width of the 	window.                                        
    CDC   dcBmp;                                           
    dcBmp.CreateCompatibleDC(&dc);                         
    CBitmap   bmpBackground;     
    bmpBackground.LoadBitmap(IDB_BITMAPBG);                 
    BITMAP m_bitmap;                                                     
    bmpBackground.GetBitmap(&m_bitmap);                    
    CBitmap   *pbmpOld=dcBmp.SelectObject(&bmpBackground);
```
