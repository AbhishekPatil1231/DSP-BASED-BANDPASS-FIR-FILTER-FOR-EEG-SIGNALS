`timescale 1ns / 1ps
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    11:32:10 04/27/2025 
// Design Name: 
// Module Name:    dsp_filter 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module dsp_filter(
    input clk,
    input rst,
    input [15:0] eeg_samples,
    output reg [31:0] filtered_out
    );

parameter N =64;
parameter half_N = N / 2;
reg signed [15:0] x[0:N-1];
reg signed [15:0] h[0:half_N-1];
reg signed [31:0] temp_sum;
integer i;

initial 
begin 
    $readmemh("C:/Pro/mp/alpha.txt",h);
end

always @(posedge clk) begin
    if (rst) begin
        for (i = 0; i <64; i = i + 1)
		       x[i] <= 0;
		  filtered_out <= 0;
   
        
    end
    else 
    begin
        // Shift the samples
        for (i =64-1; i > 0; i = i - 1)
        
            x[i] = x[i - 1];
        
        x[0] = eeg_samples;

        // Reset temp_sum for the new calculation
        temp_sum = 0;

        // Calculate the filtered output
        for (i = 0; i < 64/2; i = i + 1)
        
            temp_sum = temp_sum + (h[i] * (x[i] + x[64- 1 - i]));
				
        
        filtered_out <= temp_sum;
		  
    end 
end
endmodule

