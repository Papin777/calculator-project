from utils import add, subtract, multiply, divide

def main():
    while True:
        print("\n=== Calculatrice ===")
        print("1. Addition")
        print("2. Soustraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quitter")

        choix = input("Votre choix : ")

        if choix == '5':
            print("Au revoir !")
            break

        if choix not in ['1', '2', '3', '4']:
            print("Choix invalide. Veuillez réessayer.")
            continue

        try:
            n1 = float(input("Entrez le premier nombre : "))
            n2 = float(input("Entrez le deuxième nombre : "))
        except ValueError:
            print("Erreur : Veuillez entrer des nombres valides.")
            continue

        try:
            if choix == '1':
                print(f"Résultat : {add(n1, n2)}")
            elif choix == '2':
                print(f"Résultat : {subtract(n1, n2)}")
            elif choix == '3':
                print(f"Résultat : {multiply(n1, n2)}")
            elif choix == '4':
                print(f"Résultat : {divide(n1, n2)}")
        except ValueError as e:
            print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
