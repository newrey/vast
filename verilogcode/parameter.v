module led #
  (
   parameter PARA0 = 10,
   parameter PARA1 = 20,
   parameter PARA2 = 30, PARA3 = 40
   )
  (
   input CLK,
   input RST,
   output reg [7:0] LED
   );
  
endmodule
