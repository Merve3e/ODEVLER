class StringTarihIslemi
{
    static void Main()
    {
        string s1 = "22.04.2020";

        //tarihin yıl kısmını alınız
        string yil = s1.Split(".")[2];
        string ay = s1.Substring(3, 2);

        Console.WriteLine("Yıl: " + yil);
        Console.WriteLine("Ay: " + ay);

        Console.ReadLine();
    }
}
using System;

class Program
{
    static List<string> kelimeler = new List<string> { "bir", "iki", "üç", "dört", "beş" };
    static string[] kelimeDizisi = new string[] { "bir", "iki", "üç", "dört", "beş"};

    static void Main()
    {
        kelimeler.Add("altı");

        kelimeler.Remove("üç");

        kelimeler[2] = "sekiz";

        Console.WriteLine("Liste Elemanları:");
        foreach(string k in kelimeler)
        {
            Console.WriteLine(k);
        }

        Console.ReadLine();
    }

    static void main()
    {
        string[] temp = kelimeDizisi;
        kelimeDizisi = new string[kelimeDizisi.Length + 1];

        for(int i = 0; i < temp.Length; i++)
        {
            kelimeDizisi[i] = temp[i];
        }
        kelimeDizisi[5] = "altı";

        for(int i = 0; i < kelimeDizisi.Length; i++)
        {
            if (kelimeDizisi[i] == "üç")
            {
                kelimeDizisi[i] = "";
            }
        }

        kelimeDizisi[2] = "sekiz";

        Console.WriteLine("Liste Elemanları:");
        foreach (string k in kelimeDizisi)
        {
            Console.WriteLine(k);
        }

        Console.ReadLine();
    }

}class DegistirmeIslemi
{
    static void Main()
    {
        Console.Write("Metin Girin");
        string metin1 = Console.ReadLine();

        Console.Write("Değiştirilecek Kelimeyi Girin:");
        string metin2 = Console.ReadLine();

        Console.Write("Yeni Kelime:");
        string metin3 = Console.ReadLine();

        metin1 = metin1.Replace(metin2, metin3);


        Console.WriteLine(metin1);
        Console.ReadLine();
    }
}


using System;

public class Sihirbaz
{
    private string isim;
    private int yas;
    private string altKahveTuru;

    public int Yas
    {
        get { return yas; }
        set {

            if (value > 3 && value < 75)
            {
                yas = value;
            }
            else
            {
                Console.WriteLine("Yaş 3 ile 75 arasında olmalıdır");
            }
        }
    }

    public string İsim
    {
        get { return isim; }
        set { isim = value; }
    }

    public string KahveTuru
    {
        get
        {
            return altKahveTuru;
        }
        set
        {
            if (value == "sade" || value == "sütlü")
            {
                altKahveTuru = value;
            }
            else
            {
                Console.WriteLine("Sadece sütlü ya da sade seçnekleri vardır.");
            }
        }
    }

    public void SihirbazBilgileriGöster()
    {
        Console.WriteLine("Sihirbazın ismi: " + İsim);
        Console.WriteLine("Sihirbazın yaşı: " + Yas);
        Console.WriteLine("Sihirbazın sevdiği kahve türü: " + KahveTuru);
    }
}

class Program
{
    static void Main()
    {
        Sihirbaz sihirbaz = new Sihirbaz();

        sihirbaz.İsim = "Doruk";
        sihirbaz.Yas = 26;
        sihirbaz.Yas = 99;

        Console.WriteLine(sihirbaz.Yas);

        sihirbaz.KahveTuru = "Musluk Suyu";
        Console.WriteLine(sihirbaz.KahveTuru);
        sihirbaz.KahveTuru = "sade";
        Console.WriteLine(sihirbaz.KahveTuru);
        sihirbaz.SihirbazBilgileriGöster();
        Console.ReadLine();
    }
}