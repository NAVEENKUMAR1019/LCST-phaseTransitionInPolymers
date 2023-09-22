      program pdbread
        implicit none
        integer :: i ,j,n
        integer::noa
        integer::resid

c        !noa=====> number of atoms
c        !x,y,z=====> co-ordinates
        character(len=6),dimension(:),allocatable::fl
        character(len=6)::lf
        character(len=4)::atmty
        character(len=3)::res
        character(len=1)::axx
        real::x,y,z
        character*78::cc

10        format(6a)    
20        format(a6,2x,3i,1x,4a,1x,3a,1x,1a,
     &2x,2i,5x,f7.3,1x,f7.3,1x,f7.3,24x)
30        format(4a,1x,f7.3,1x,f7.3,1x,f7.3)
40        format(12x,4a,f7.3,1x,f7.3,1x,f7.3)
50        format(a78)


       open(unit=1,file="1p-elp_clp_1-1500_pep-mini.pdb",status="old")
       write(*,*)" get the number of lines to read from the user"
       read(*,*)n
       write(*,*)n
   
        
        allocate(fl(n))
        do i=1,n
        read(1,10)fl(i)
        end do
      
        close(1)

        open(unit=2,file="1p-elp_clp_1-1500_pep-mini.pdb",status="old")
        open(unit=3,file="atomtype_co-ordinates.txt",status="old")
        open(unit=4,file="energies.txt",status="old")
        do i=1,n  

        read(2,50)cc
            if( fl(i).eq."ATOM")then
                write(3,50)cc
        elseif(fl(i).eq."MODEL")then
                write(4,50)cc
        end if
        end do     
        deallocate(fl)
        close(2)
        close(3)
        close(3)
      end program 

