      program main


c    $$$$$$$$$$$$$$$$ section 1 $$$$$$$$$$$$$$$$$

              implicit none
              integer::i,j,n,nos,noa
              character(len=6),dimension(:),allocatable::atmty
              real,dimension(:),allocatable::x,y,z,r
              real,dimension(:,:),allocatable::Xx,Yy,Zz
              real,dimension(:),allocatable::mass,srog,rog!,energies
              real::mos
             
              !ede===>> end to end distance
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
                

c#########################################################################
c              this program reads the co ordinate files and find the     #
c distance of each atom ... the vector r(i) have the distance of all     #
c atoms ..... the matrix Rr(i,J) has nos rows each row corresponds to a  #
c particular structures and entries in the rows is the distance of all   #
c atoms in that particular structures                                    #
c ########################################################################

         write(*,*) "enter the number of structures  "
              read(*,*)nos
         write(*,*)"enter the number of atoms in a single structure"
              read(*,*)noa
         write(*,*)"enter the total number of atoms in the files...
     &(number of atoms in one structures x total number of structures"
         print*,nos*noa
            read(*,*)n
         
          allocate(atmty(n),mass(n),x(n),y(n),z(n),r(nos),Xx(nos,noa),
     &Yy(nos,noa),Zz(nos,noa))

10            format(12x,a4,14x,3f8.3)

              open(unit=1,file="atomtype_co-ordinates.txt",status="old")
               do i=1,n
               read(1,10)atmty(i),x(i),y(i),z(i)
c               write(*,10)atmty(i),x(i),y(i),z(i)
               end do
            
           do i=1,nos
                do j=1,noa
                    Xx(i,j)=x(noa*(i-1)+j)
                    Yy(i,j)=y(noa*(i-1)+j)
                    Zz(i,j)=z(noa*(i-1)+j)
                    end do
                    end do
c             ! finding end to end  distace r
      do i=1,nos
      r(i)=sqrt(((Xx(i,noa)-Xx(i,1))*(Xx(i,noa)-Xx(i,1))) +
     &((Yy(i,noa)-Yy(i,1))*(Yy(i,noa)-Yy(i,1))) +
     &((Zz(i,noa)-Zz(i,1))*(Zz(i,noa)-Zz(i,1))))     

             end do
c             print*,r
             close(1)

c there are number of rows as number of structures , each row 
c has distance r of each atom in that structure


c#######################################################################
c             end to end distance of each structure                    #
c                                                                      #
c   each row in Rr correspond to a single structure                    #
c   subtracting the value of first and last element in each row gives  # 
c     the end to end distance of each structures                       #
c#######################################################################


           

             open(unit=3,file="E_2_E_distance.txt",status="old")
             do i=1,nos
             write(3,*)r(i)

             enddo

       deallocate(atmty,mass,x,y,z,r,Xx,Yy,Zz)

      end program
