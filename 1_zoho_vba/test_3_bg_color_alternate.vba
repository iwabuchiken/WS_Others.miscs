Sub test_3_bg_color_alternate()
'  
'  test_2 Macro
'  Created by iwabuchi.k.2010 on 2019年5月22日 10:07:05
'  
'  get row number; if it is an odd number, then get the cell bg color to yellow.
'  
	
    '==================================================
    '	A : 1
    '==================================================
    '=========================
    '	prep : var
    '=========================
	Dim ColumnNumber As Long
	Dim RowNumber As Long
	
	Dim numOf_Selection_Members As Long
	
    '=========================
    '	get : selection
    '=========================
    'Selection.Interior.Color = 13995605
    
    'numOf_Selection_Members = Selection.count
    numOf_Selection_Members = Selection.rows.count
    
    '=========================
    '	op : each item in the selection
    '=========================
    
    '=========================
    '	report
    '=========================
    MsgBox "numOf_Selection_Members : " & numOf_Selection_Members

    '==================================================
    '	A : 2 : 
    '==================================================
	'ref https://vbmacros.wiki.zoho.com/Lightening-Colors.html
	Set Rng = Selection
	
	Dim strOf_Odd As String
	Dim strOf_Even As String
	
	For I = 2 To Rng.Cells.Count
		
		
		
		'Rng.Cells(I).Text = "I = " & I
		'Rng.Cells(I).value = "Cells(" & I & ").Column = " & Rng.Cells(I).Column
		'Rng.Cells(I).value = "Cells(" & I & ").Row = " & Rng.Cells(I).Row
		'Rng.Cells(I).value = "Cells(" & I & ").Row + 1 = " & (Rng.Cells(I).Row + 1)
		
		'ref MOD https://stackoverflow.com/questions/4378047/vba-equivalent-to-excels-mod-function
		Rng.Cells(I).value = "Cells(" & I & ").Row MOD 2 = " & (Rng.Cells(I).Row MOD 2)
		
		'If Rng.Cells(I).Row % 2 == 0 Then
		'If ((Rng.Cells(I).Row MOD 2) == 1) Then
		If ((Rng.Cells(I).Row MOD 2) = 1) Then
			
			Rng.Cells(I).Interior.Color = 13995605
			
		End If
		
'     With Rng.Cells(I).Interior
'          .Color = RGB(R + (255 - R) * (I - 1) / (Rng.Cells.Count - 1), _
'                 G + (255 - G) * (I - 1) / (Rng.Cells.Count - 1), _
'                 B + (255 - B) * (I - 1) / (Rng.Cells.Count - 1))
'     End With
	Next I
	
End Sub
