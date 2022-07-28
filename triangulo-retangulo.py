# Escreva, na classe Triangulo, o método retangulo() que devolve True se o triângulo for retângulo, e False caso contrário.
if(__name__)=='__main__':
    class Triangulo():
        def __init__(self,a,b,c):
            self.a=a
            self.b=b
            self.c=c
        def perimetro(self):
            self.perim=((self.a)+(self.b)+(self.c))
            return self.perim
        def semelhantes(self,triangulo):
            triangulo_1=[self.a,self.b,self.c]
            triangulo_2=[triangulo.a,triangulo.b,triangulo.c]
            sorted(triangulo_1)
            sorted(triangulo_2)
            if triangulo_1[0]/triangulo_2[0]==triangulo_1[1]/triangulo_2[1]==triangulo_1[2]/triangulo_2[2]:
                return True
            else:
                return not True
        def tipo_lado(self):
            tipo_lado=['isósceles','equilátero','escaleno']
            if((self.a)==(self.b))and((self.a)==(self.c)):
                return tipo_lado[1]
            elif((self.a)!=(self.b))and((self.a)!=(self.c)):
                return tipo_lado[2]
            else:
                return tipo_lado[0]
        def retangulo(self):
            if((self.a)>(self.b))and((self.a)>(self.c)):
                self.h=self.a
                self.co=self.b
                self.ca=self.c
            elif((self.b)>(self.a))and((self.b)>(self.c)):
                self.h=self.b
                self.co=self.c
                self.ca=self.a
            elif((self.c)>(self.a))and((self.c)>(self.b)):
                self.h=self.c
                self.co=self.a
                self.ca=self.b
            else:
                return not True
            if(self.h**2==(self.co**2)+(self.ca**2)):
                return True
            else:
                return not True
        pass
# O resultado dos testes com seu programa foi:
# Parabéns! Todos os testes tiveram sucesso!