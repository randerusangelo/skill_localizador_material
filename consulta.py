import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

def buscar_localizacao(material_nome):
    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={os.getenv('DB_SERVER')};"
            f"DATABASE={os.getenv('DB_NAME')};"
            f"UID={os.getenv('DB_USER')};"
            f"PWD={os.getenv('DB_PASSWORD')};"
            f"Trusted_Connection=no;"
            f"Network=DBMSSOCN;"
        )
        cursor = conn.cursor()
        query = """
            
        SELECT 
            E.nome,
            L.setor  
        FROM produtos as E
            left join localizacoes L on E.localizacao_id = L.id
            WHERE E.nome LIKE ?
        """
        cursor.execute(query, f"%{material_nome}%")
        rows = cursor.fetchall()
        conn.close()

        if rows:
            resposta = f"Encontrei {len(rows)} iten"
            resposta += "s" if len(rows) > 1 else ""
            resposta += ": "

            for row in rows:
                nome, setor = row
                resposta += f"{nome} está no setor {setor}. <break time='0.5s'/> "

            return resposta
        else:
            return "Desculpe, não encontrei esse material no sistema."
        
    except Exception as e:
        return f"Ocorreu um erro ao buscar o material: {str(e)}"


if __name__ == "__main__":
    termo = input("Digite o nome (ou parte) do material para buscar: ")
    print(buscar_localizacao(termo))
