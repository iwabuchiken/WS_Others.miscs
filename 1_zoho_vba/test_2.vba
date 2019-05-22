Sub test_2()
'  
'  test_2 Macro
'  Created by iwabuchi.k.2010 on 2019年5月22日 10:07:05
'  
'  get row number; if it is an odd number, then get the cell bg color to yellow.
'  
	
    '=========================
    '	prep : var
    '=========================
	Dim ColumnNumber As Long
	Dim RowNumber As Long

    '=========================
    '	get : selection
    '=========================
    'Range("C6").Select
    
    Selection.Interior.Color = 13995605
    
    '=========================
    '	get : col num
    '=========================
    ColumnNumber = Selection.Column
    
    '=========================
    '	get : row num
    '=========================
    RowNumber = Selection.Row
    
    '=========================
    '	display
    '=========================
    MsgBox "Column : " & ColumnNumber & " / " & "Row : " & RowNumber
    
End Sub