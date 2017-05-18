package sql;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class CargarJuegos {
	
	/*public static void main(String Args[]) throws IOException{
		File file=new File("C:/Users/Alfonso/Downloads/juegos3.sql");
		File file2=new File("C:/Users/Alfonso/Downloads/juegos4.sql");
		BufferedReader br= new BufferedReader(new FileReader(file));
		BufferedWriter bw = new BufferedWriter(new FileWriter(file2));
		String linea;
		int i=0;
		while((linea=br.readLine())!=null){
			i++;
			int inicio=linea.indexOf("'http");
			String c1=linea.substring(0,inicio);
			String c=linea.substring(inicio);
			int fin=c.indexOf(",'");
			String c2=c.substring(fin+1);
			bw.write(c1+c2+"\n");
			//System.out.println(i);
		}
		
		
	}*/
	
	public static void main(String Args[]) throws IOException{
		File file=new File("C:/Users/Alfonso/Downloads/juegos4.sql");
		BufferedReader br= new BufferedReader(new FileReader(file));
		File file2=new File("C:/Users/Alfonso/Downloads/juegos.sql");
		BufferedWriter bw = new BufferedWriter(new FileWriter(file2));
		File file3=new File("C:/Users/Alfonso/Downloads/plataforma.sql");
		BufferedWriter bw2 = new BufferedWriter(new FileWriter(file3));
		File file4=new File("C:/Users/Alfonso/Downloads/genero.sql");
		BufferedWriter bw3 = new BufferedWriter(new FileWriter(file4));
		File file5=new File("C:/Users/Alfonso/Downloads/desarrolladora.sql");
		BufferedWriter bw4 = new BufferedWriter(new FileWriter(file5));
		File file6=new File("C:/Users/Alfonso/Downloads/juego_plataforma.sql");
		BufferedWriter bw5 = new BufferedWriter(new FileWriter(file6));
		File file7=new File("C:/Users/Alfonso/Downloads/juego_genero.sql");
		BufferedWriter bw6 = new BufferedWriter(new FileWriter(file7));
		File file8=new File("C:/Users/Alfonso/Downloads/juego_desarrolladora.sql");
		BufferedWriter bw7 = new BufferedWriter(new FileWriter(file8));
		
		String linea;
		int i=0;
		String [] juegos = new String[37204];
		String [] plataformas = new String[37204];
		String [] generos = new String[37204];
		String [] companias = new String[37204];
		int [][] jp = new int[37204][2];
		for(int x=0;x<jp.length;x++){
			jp[x][0]=-1;
		}
		int [][] jg = new int[37204][2];
		for(int x=0;x<jp.length;x++){
			jg[x][0]=-1;
		}
		int [][] jc = new int[37204][2];
		for(int x=0;x<jp.length;x++){
			jc[x][0]=-1;
		}
		int jID=0;
		int pID=0;
		int gID=0;
		int cID=0;
		int jpID=0;
		int jgID=0;
		int jcID=0;
		
		//while(i<37204){
		while(i<37204){
			linea=br.readLine();
			i++;
			int inicio=linea.indexOf("VALUES (");
			int finJuego=linea.indexOf(",'");
			String juego=linea.substring(inicio+8,finJuego);
			if(insertarJuego(juegos,juego,jID)!=-1){
				bw.write("\nINSERT INTO videojuego(id,titulo,puntnMedia) VALUES ("+(jID+1)+","+juego+",0);");
				jID++;
			}

			String sub1=linea.substring(finJuego+1);
			int finPlataforma=sub1.indexOf(",'");
			String plataforma=sub1.substring(0,finPlataforma);
			if(insertar(plataformas,plataforma)!=-1){
				bw2.write("\nINSERT INTO plataforma(id,nombre) VALUES ("+(pID+1)+","+plataforma+");");
				pID++;
			}
			
			String sub2=sub1.substring(finPlataforma+1);
			int finGenero=sub2.indexOf(",'");
			String genero=sub2.substring(0,finGenero);
			if(insertar(generos,genero)!=-1){
				bw3.write("\nINSERT INTO genero(id,nombre) VALUES ("+(gID+1)+","+genero+");");
				gID++;
			}
		
			String sub3=sub2.substring(finGenero+1);
			int finCompania=sub3.indexOf(")");
			String compania=sub3.substring(0,finCompania);
			if(insertar(companias,compania)!=-1){
				bw4.write("\nINSERT INTO desarrolladora(id,nombre) VALUES ("+(cID+1)+","+compania+");");
				cID++;
			}
			
			
			
			if(insertar(jp,jID,pID,jpID)!=-1){
				bw5.write("\nINSERT INTO plataforma_videojuego(id,id_videojuego,id_plataforma) VALUES ("+(jpID+1)+","+(buscar(juegos,juego)+1)+","+(buscar(plataformas,plataforma)+1)+");");
				jpID++;
			}
			if(insertar(jg,jID,gID,jgID)!=-1){
				bw6.write("\nINSERT INTO genero_videojuego(id,id_videojuego,id_genero) VALUES ("+(jpID+1)+","+(buscar(juegos,juego)+1)+","+(buscar(generos,genero)+1)+");");
				jgID++;
			}
			if(insertar(jc,jID,cID,jcID)!=-1){
				bw7.write("\nINSERT INTO desarrolladora_videojuego(id,id_videojuego,id_desarrolladora) VALUES ("+(jpID+1)+","+(buscar(juegos,juego)+1)+","+(buscar(companias,compania)+1)+");");
				jcID++;
			}
	
		}
		bw.close();
		bw2.close();
		bw3.close();
		bw4.close();
		bw5.close();
		bw6.close();
		bw7.close();
		
	}
	
	
	public static int insertarJuego(String [] array,String dato,int indice){

		if(indice-1>=0 && array[indice-1].compareTo(dato)==0){
			return -1;
		}
		else{
			array[indice]=dato;
			return indice+1;
		}
	}
	
	public static int insertar(String [] array,String dato){
		int i;
		if(array[0]==null){
			array[0]=dato;
			return 0;
		}
		else{
			for(i=0;i<array.length && array[i]!=null;i++){
				if(array[i].compareTo(dato)==0){
					return -1;
				}
			}
		}
		array[i]=dato;
		return i;
	}
	
	public static int insertar(int [][] array,int dato,int dato2,int indice){
		int i=0;
		if(array[0][0]==-1){
			array[0][0]=dato;
			array[0][1]=dato2;
			return 0;
		}
		else{
			for(i=0;i<array.length && array[i][0]!=-1;i++){
				if((array[i][0]==dato && array[i][1]==dato2)){
					return -1;
				}
			}
		}
		array[i][0]=dato;
		array[i][1]=dato2;
		return i;
	}
	
	public static int buscar(String [] array,String dato){
		int i;
		if(array[0]==null){
			return 0;
		}
		else{
			for(i=0;i<array.length && array[i]!=null;i++){
				if(array[i].compareTo(dato)==0){
					return i;
				}
			}
		}
		return i;
	}
	
	
}
