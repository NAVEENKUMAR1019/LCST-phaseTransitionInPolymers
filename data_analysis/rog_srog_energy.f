      program main


c    $$$$$$$$$$$$$$$$ section 1 $$$$$$$$$$$$$$$$$

              implicit none
              integer::i,j,n,nos,noa
              character(len=6),dimension(:),allocatable::atmty
              real,dimension(:),allocatable::x,y,z,r
              real,dimension(:,:),allocatable::Rr,Rr2,Mm,Ssrog
              real,dimension(:),allocatable::mass,srog,rog!,energies
              real::mos
             

              !mas==>>mass of a single structure
              !nos==>>number of structures
              !noa==> number of atoms in a single structures
              !atmty==> is the array ,type of all atom in the file



c    $$$$$$$$$$$$$$  section 2 $$$$$$$$$$$$$$$$$
               !temporary not general variables....its for just 
               !check and assign 

              character(len=6)::c_atmty(67)
              real::c_mass(67)  
              character(len=9)::xxxx
              integer::yyyy          
                


c          comments ########################
c              this program reads the co ordinate files and find the
c distance of each atom ... the vector r(i) have the distance of all
c atoms ..... the matrix Rr(i,J) has nos rows each row corresponds to a
c particular structures and entries in the rows is the distance of all
c atoms in that particular structures
c

         write(*,*) "enter the number of structures  "
              read(*,*)nos
         write(*,*)"enter the number of atoms in a single structure"
              read(*,*)noa
         write(*,*)"enter the total number of atoms in the files...
     &(number of atoms in one structures x total number of structures"
         print*,nos*noa
            read(*,*)n
         
          allocate(atmty(n),mass(n),x(n),y(n),z(n),r(n))

10            format(12x,a4,14x,3f8.3)

              open(unit=1,file="atomtype_co-ordinates.txt",status="old")
               do i=1,n
               read(1,10)atmty(i),x(i),y(i),z(i)
c               write(*,10)atmty(i),x(i),y(i),z(i)
               end do
             
            ! finding distace r
             do i=1,n
             r(i)=sqrt( x(i)*x(i) + y(i)*y(i) + z(i)*z(i) )
             end do
            ! print*,r
             close(1)






c sepearting the structures and putting into a matrix
c there are number of rows as number of structures , each row 
c has distance r of each atom in that structure

             allocate(Rr(nos,noa))
             allocate(Rr2(nos,noa))
             
             open(unit=2,file="atomtype_co-ordinates.txt",status="old")
             do i=1,nos
                do j=1,noa
                    Rr(i,j)=r(noa*(i-1)+j) - 100.6996
                    end do
                    end do
c                    write(*,*)Rr(1,:)

c                    write(*,*)Rr(2,:)

             close(2)
c creating Rr2 ( which is nothing but distance squared)
                
                do i = 1,nos
                  do j= 1,noa
                    Rr2(i,j)=Rr(i,j)*Rr(i,j)
                    end do
                    end do
!                    write(*,*)Rr
!                    write(*,*)Rr2




c reading the mass of each atom from the mass library mass.txt and
c assinging the value of mass to each atom in the atmty(i)

             open(unit=3,file="mass.txt",status="old")
21         format(a4,f7.4)
23         format(4a)
             do i=1,67
             read(3,21)c_atmty(i),c_mass(i)
             end do
            
!            write(*,*) c_atmty
!           write(*,*) c_mass
          
c here mass are taken as as atomic mass unit....
c for finding the radius of gyration k= sqrt(I/M)....it won't cause 
c any problem..... but for finding the actuall value of mass we have to
c multiply the atomic mass unit by 1.66054e-27 kg.....

22         format(f7.4) 
            
               do i=1,n
                 do j=1,67
                  if(atmty(i).eq.c_atmty(j))then
                         mass(i)=c_mass(j)
                  end if
                 end do
                end do 

c creating mass matrix Mm
c #######################
            allocate(Mm(nos,noa))

       do i =1,nos
          do j=1,noa
            Mm(i,j)=mass(noa*(i-1)+j)
            end do
            end do

c     mos==> mass of a single structure
          mos=sum(Mm(1,:))      

c finding radius of gyration maytrix
c Ssrog is a matrix in which each element is the product of 
c its mass and squared distance from the centre of mass
c we can get the squared radius of gyration of each structures by adding all elements
c in each row and dividing it by mass of a single structure i.,mos

!   srog==> squared radius of gyration
!    rog==> radius of gyration

          allocate(Ssrog(nos,noa))
          allocate(srog(nos))
          allocate(rog(nos))
         do i=1,nos
           do j=1,noa
             Ssrog(i,j)=Mm(i,j)*Rr2(i,j)
           end do
          end do

              do i=1,nos
               srog(i)=(sum(Ssrog(i,:)))/mos
                end do
                do i=1,nos
                rog(i)=sqrt(srog(i))
                  end do
c reading energies from energies.text file 
c        open(unit=4,file="energies.txt",status="old")
c        allocate(energies(n))
c       
c05        format(a9,i4,f13.2)
c
c       do i=1,nos
c       read(4,05)xxxx,yyyy,energies(i)
c       end do
c
c       write(*,05)xxxx,yyyy,energies


c writing the all colected data in a text file radius_of_gyration.txt
       open(unit=5,file="radius_of_gyration.txt",status="old")
       
       
           
           do i = 1,nos
              write(5,*)i,rog(i),srog(i)
              end do
c              write(5,*)(sum(rog(:)))/nos
c              write(5,*)(sum(srog(:)))/nos
c              write(5,*)mos
!              write(5,*)"average_radius_of_gyration"
!              write(5,*)"average squared_radius_of_gyration"
!              write(5,*)"mass of a single structure"


            

        deallocate(atmty,mass,x,y,z,r,Rr,Rr2,Mm,Ssrog,srog,rog)!,energies)
      end program
