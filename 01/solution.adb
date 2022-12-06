with Ada.Text_IO; use Ada.Text_IO;

procedure solution is
    F                         : File_Type;
    File_Name                 : constant String := "input.txt";
    p            	      : Positive;
    Elf, Largest_Elf          : Integer := 0;
    Current_Line              : String := "";
begin
    --get(p);
    --declare
    --    Elves : array(1 .. p) of Integer;
    --begin
    --Create (F, Out_File, File_Name);
    Open(F, Out_File, File_Name);
    while not End_Of_File(F) loop
	Current_Line := Get_Line(F);
	Put_Line(Current_Line);
        if Current_Line = "\n" then
	    -- put(Elves(Integer'Value(Current_Line));
	    if Elf > Largest_Elf then
		Largest_Elf := Elf;
	    end if;
	    Elf := 0;
	else
	    Elf := Elf + Integer'Value(Current_Line);
	end if;
    end loop;
    Ada.Text_IO.Put_Line(Integer'Image(Largest_Elf));
end solution;
