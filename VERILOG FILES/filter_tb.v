`timescale 1ns / 1ps

module fir_symmetric_filter_tb;

    // Clock and reset
    reg clk;
    reg rst;

    // DUT inputs and outputs
    reg signed [15:0] sample_in;
    wire signed [31:0] filtered_out;

    // File handling
    integer input_file, output_file;
    integer status;
    reg signed [15:0] sample_array [0:1023];  // Adjust size if needed (here max 1024 samples)
    integer sample_index;

    // Instantiate your filter
    fir_symmetric_filter uut (
        .clk(clk),
        .rst(rst),
        .sample_in(sample_in),
        .filtered_out(filtered_out)
    );

    // Clock generation: 10ns period (100MHz)
    initial begin
        clk = 0;
        forever #5 clk = ~clk;   // Toggle every 5ns => 10ns period
    end

    // Testbench procedure
    initial begin
        // Open input and output files
        $readmemh("input.txt", sample_array);    // Read hex values into array
        output_file = $fopen("output.txt", "w"); // Open output file to write
        
        // Reset
        rst = 1;
        sample_in = 0;
        sample_index = 0;
        #20;            // Hold reset for 20ns
        rst = 0;

        // Feed samples one by one
        for (sample_index = 0; sample_index < 256; sample_index = sample_index + 1) begin
            sample_in = sample_array[sample_index];
            @(posedge clk);  // Wait for clock edge
            
            // Write output after some delay to allow processing (1 clock later here)
            @(posedge clk);
            $fwrite(output_file, "%08X\n", filtered_out);  // Save 32-bit output in HEX
        end

        // Finish
        $fclose(output_file);
        $stop;
    end

endmodule
