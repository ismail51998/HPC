module mod_ods6ojc1800f_ods6ojc1800f

use, intrinsic :: ISO_C_BINDING

implicit none

contains

!........................................
function solve_2d_nonlinearconv_pyccel(u, un, v, vn, nt, dt, dx, dy, c) &
      result(Out_0001)

  implicit none

  integer(C_INT64_T) :: Out_0001
  real(C_DOUBLE), intent(inout) :: u(0:,0:)
  real(C_DOUBLE), intent(inout) :: un(0:,0:)
  real(C_DOUBLE), intent(inout) :: v(0:,0:)
  real(C_DOUBLE), intent(inout) :: vn(0:,0:)
  integer(C_INT64_T), value :: nt
  real(C_DOUBLE), value :: dt
  real(C_DOUBLE), value :: dx
  real(C_DOUBLE), value :: dy
  integer(C_INT64_T), value :: c
  integer(C_INT64_T) :: row
  integer(C_INT64_T) :: col
  integer(C_INT64_T) :: t
  integer(C_INT64_T) :: i
  integer(C_INT64_T) :: j

  !##Assign initial conditions
  !#set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
  u(Int(0.5_C_DOUBLE / dx, C_INT64_T):Int(1_C_INT64_T / dx + 1_C_INT64_T &
      , C_INT64_T) - 1_C_INT64_T, Int(0.5_C_DOUBLE / dy, C_INT64_T):Int &
      (1_C_INT64_T / dy + 1_C_INT64_T, C_INT64_T) - 1_C_INT64_T) = &
      2_C_INT64_T
  !#set hat function I.C. : v(.5<=x<=1 && .5<=y<=1 ) is 2
  v(Int(0.5_C_DOUBLE / dx, C_INT64_T):Int(1_C_INT64_T / dx + 1_C_INT64_T &
      , C_INT64_T) - 1_C_INT64_T, Int(0.5_C_DOUBLE / dy, C_INT64_T):Int &
      (1_C_INT64_T / dy + 1_C_INT64_T, C_INT64_T) - 1_C_INT64_T) = &
      2_C_INT64_T
  row = size(u, 2_C_INT64_T, C_INT64_T)
  col = size(u, 1_C_INT64_T, C_INT64_T)
  do t = 0_C_INT64_T, nt - 1_C_INT64_T, 1_C_INT64_T
    do i = 1_C_INT64_T, row - 1_C_INT64_T, 1_C_INT64_T
      do j = 1_C_INT64_T, col - 1_C_INT64_T, 1_C_INT64_T
        un(j, i) = u(j, i)
        vn(j, i) = v(j, i)
      end do
    end do
    do i = 1_C_INT64_T, row - 1_C_INT64_T, 1_C_INT64_T
      do j = 1_C_INT64_T, col - 1_C_INT64_T, 1_C_INT64_T
        u(j, i) = un(j, i) - un(j, i) * dt * (un(j, i) - un(j, i - &
      1_C_INT64_T)) / dx - vn(j, i) * dt * (un(j, i) - un(j - &
      1_C_INT64_T, i)) / dy
        v(j, i) = vn(j, i) - un(j, i) * dt * (vn(j, i) - vn(j, i - &
      1_C_INT64_T)) / dx - vn(j, i) * dt * (vn(j, i) - vn(j - &
      1_C_INT64_T, i)) / dy
      end do
    end do
  end do
  Out_0001 = 0_C_INT64_T
  return

end function solve_2d_nonlinearconv_pyccel
!........................................

end module mod_ods6ojc1800f_ods6ojc1800f
