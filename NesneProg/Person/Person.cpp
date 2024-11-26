#include <iostream>
#include <string>
using std::string;

class Person {
protected:
    string name;
    int age;

public:
    Person(string n, int a) : name(n), age(a) {}

    string getName() { return name; }
    void setName(string n) { name = n; }

    int getAge() { return age; }
    void setAge(int a) { age = a; }

    virtual void display() {
        std::cout << "Name: " << name << "\nAge: " << age << std::endl;
    }
};

class Student : public Person {
private:
    string studentID;

public:
    Student(string n, int a, string id) : Person(n, a), studentID(id) {}

    string getStudentID() { return studentID; }
    void setStudentID(string id) { studentID = id; }

    void display() override {
        Person::display();
        std::cout << "Student ID: " << studentID << std::endl;
    }
};

class Teacher : public Person {
private:
    string subject;

public:
    Teacher(string n, int a, string sub) : Person(n, a), subject(sub) {}

    string getSubject() { return subject; }
    void setSubject(string sub) { subject = sub; }

    void display() override {
        Person::display();
        std::cout << "Subject: " << subject << std::endl;
    }
};

int main() {
    Person person1("Hakan Tunc", 46);
    std::cout << "Person:" << std::endl;
    person1.display();
    std::cout << std::endl;

    Student student1("Deniz Kaya", 20, "218480");
    std::cout << "Ogrenci :" << std::endl;
    student1.display();
    std::cout << std::endl;

    Student student2("Kaan Gunay", 21, "263551");
    std::cout << "Ogrenci :" << std::endl;
    student2.display();
    std::cout << std::endl;

    Teacher teacher1("Yeliz Can", 33, "Tarih");
    std::cout << "Ogretmen:" << std::endl;
    teacher1.display();
    std::cout << std::endl;

    return 0;
}
