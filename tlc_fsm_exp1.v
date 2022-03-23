`timescale 1ns/1ps
`default_nettype none

`define one_sec 50000000
`define three_sec 150000000
`define thirty_sec 1500000000
`define fifteen_sec 750000000

module tlc_fsm_exp1(
    output reg [2:0] state, 		//output for debugging
    output reg RstCount,			//use an always block
    output reg [1:0] highwaySignal, farmSignal,
    input wire [30:0] Count, 		//use n computed earlier
    input wire Clk, Rst 			//clock and reset
);

//defining states
parameter 	Srst = 3'b110,
	  	S0 = 3'b000,
          		S1 = 3'b001,
         		S2 = 3'b010,
          		S3 = 3'b011,
          		S4 = 3'b100,
          		S5 = 3'b101;

//defining colors
parameter 	green  = 2'b00,
          		yellow = 2'b01,
          		red    = 2'b10;
//intermediate nets
    reg [2:0] nextState;
//next state logic
always@(state or Count)
case(state)
Srst: nextState = S0;
S0: begin
if(Count == `one_sec)		//if count reached
nextState = S1; 		//transition
else //otherwise
nextState = S0; 		//remain in current state
end
S1: begin
if(Count == `thirty_sec)		//if count reached
nextState = S2; 		//transition
else //otherwise
nextState = S1; 		//remain in current state
end
S2: begin
		if(Count == `three_sec)		//if count is reached
			nextState = S3;		//transition
		else
			nextState = S2;		//remain in current state
		end
	S3: begin
		if(Count == `one_sec)		//if count is reached
			nextState = S4;		//transition
		else
			nextState = S3;		//remain in current state
		end
	S4: begin
		if(Count == `fifteen_sec)	//if count is reached
			nextState = S5;		//transition
		else
			nextState = S4;		//remain in current state
		end
S5: begin
if(Count == `three_sec)		//if count reached
nextState = S0; 		//transition
else 				//otherwise
nextState = S5; 		//remain in current state
end

default:	//avoid latches
nextState = Srst;
endcase

    /*describe output logic*/
    always@(state or Count)
        case(state)
            Srst : begin
                highwaySignal = red;
                farmSignal    = red;
                RstCount = 1;
            end
            S0: begin
                highwaySignal = red;
                farmSignal    = red;                
                if(Count == `one_sec)		//if count reached
                    RstCount = 1; 		//reset counter
                else 				//otherwise
                    RstCount = 0; 		//let counter run
            end
            S1: begin
                highwaySignal = green;
                farmSignal    = red;                
                if(Count == `thirty_sec)		//if count reached
                    RstCount = 1; 		//reset counter
                else 				//otherwise
                    RstCount = 0; 		//let counter run
            end
            S2: begin
                highwaySignal = yellow;
                farmSignal    = red;                
                if(Count == `three_sec)		//if count reached
                    RstCount = 1; 		//reset counter
                else 				//otherwise
                    RstCount = 0; 		//let counter run
            end
            S3: begin
                highwaySignal = red;
                farmSignal    = red;                
                if(Count == `one_sec)		//if count reached
                    RstCount = 1; 		//reset counter
                else //otherwise
                    RstCount = 0; 		//let counter run
            end
            S4: begin
                highwaySignal = red;
                farmSignal    = green;                
                if(Count == `fifteen_sec)	//if count reached
                    RstCount = 1; 		//reset counter
                else 				//otherwise
                    RstCount = 0; 		//let counter run
            end
            S5: begin
                highwaySignal = red;
                farmSignal    = yellow;                
                if(Count == `three_sec)		//if count reached
                    RstCount = 1; 		//reset counter
                else 				//otherwise
                    RstCount = 0; 		//let counter run
            end
          default: begin			//avoid latches!
                highwaySignal = red;
                farmSignal    = red;                
                RstCount = 1; 
end
        endcase

//the clock for the system
    always@(posedge Clk)
        if(Rst)
            state <= Srst;
        else
            state <= nextState;

endmodule
