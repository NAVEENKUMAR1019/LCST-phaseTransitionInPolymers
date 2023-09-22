      program mass
              implicit none
              integer :: i,j
              character*4atmty(67)

10     format(12x,a4)
20     format(a4)
              open(unit=1,file="inp.pdb",status="old")
              open(unit=2,file="mass.txt",status="old")
              do i=1,67
              read(1,10)atmty(i)
              write(2,20)atmty(i)
              end do
              end program
