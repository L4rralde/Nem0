#include<htc.h>

__CONFIG(FOSC_INTRC_NOCLKOUT & WDTE_OFF & PWRTE_OFF & MCLRE_OFF & CP_OFF & BOREN_OFF & IESO_OFF & FCMEN_OFF & LVP_OFF& DEBUG_OFF);
__CONFIG(BOR4V_BOR40V & WRT_OFF);

//void pause( unsigned int msvalue );		
//void msecbase( void );	


	main() {

		int envia32 = 0x6B992637;
		int recibe32, aux24;
		unsigned short aux16;
		unsigned char datotA0, datotA1, datotA2, datotA3, datotBasura, datorBasura,datorA0,datorA1,datorA2,datorA3;
		datotA0 = envia32;
		datotA1 = envia32 >> 8;
		aux24 = envia32 >> 8;
		aux16 = aux24 >> 8;
		datotA2 = aux16;
		datotA3 = aux16 >> 8;
		datotBasura = 0x33;
		
		ANSELH = 0x00; 
		ANSEL = 0x00;   
		OSCCON = 0x40;	//Oscilador interno modificado a 1MHz.
		TRISA = 0x00;	//Todos los puertos configurados como salida	 	
		TRISB = 0x00;
		TRISD = 0x00;
		TRISE = 0x00;

	//Inicialización del puerto SPI

		SSPSTAT = 0x00;
		SSPSTATbits.SMP = 0; // (slave)
		SSPSTATbits.CKE = 0; //(falling edge, SS optional (CKP = 0))
		SSPCON = 0x25;	//SLAVE MODE, SS pin control disabled;FOSC/4; CKP=0 (idle state is a LOW level); SSPEN=1(serial port enabled)
		TRISC = 0x18; //SDO=0,SCK=1, SDI=1 (Cliente)
		PIE1 = 0x00; //INTERRUPCIÓN DEL SPI INHABILITADA. SPI LISTO
		
	
		
 	//cOMIENZA TRANSMISIÓN DE DATOS	
	
		while(!BF);
		datorA0 = SSPBUF;
		SSPBUF = datotA0;
		while(!BF);
		datorA1 = SSPBUF;
		SSPBUF = datotA1;
		while(!BF);
		datorA2 = SSPBUF;
		SSPBUF = datotA2;
		while(!BF);
		datorA3 = SSPBUF;
		SSPBUF = datotA3;
		while(!BF);
		datorBasura = SSPBUF;
		SSPBUF = datotBasura;
			
		SSPCONbits.SSPEN = 0; //Desactiva puerto serial


    aux16 = (unsigned short)((datorA1 << 8) | datorA0); //parte baja del int reconstruida
	aux24 = (int)((datorA3 << 8) | datorA2);
	aux24 = aux24 << 8;
	aux24 = aux24 << 8; //parte alta del int reconstruida
	recibe32 = aux24 | aux16; //Todo el entero recibido reconstruído
		
	
		while(1) {  
		PORTA = datorA0;
		PORTB = datorA1;
		PORTD = datorA2;
		}
	
	}