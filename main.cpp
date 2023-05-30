#include <iostream>

using namespace std;

// Node Class
class Node {
public:
    int redid;
    string first;
    string last;
    Node *next;

    Node(int redid, string first, string last, Node* next) {
        this->redid = redid;
        this->first = first;
        this->last=last;
        this->next = next;
    }
};

// Linked List Class

class LinkedList {
private:
    // CLASS MEMBER VARIABLES
    Node *head;
    Node *tail;
    int length;

public:
    // LINKED LIST CONSTRUCTOR
    LinkedList() {
        head = nullptr;
        tail = nullptr;
        length = 0;
    }
    /*LinkedList(int value, string first, string last ) {
        Node *newNode = new Node(value, first, last, nullptr);
        head = newNode;
        tail = newNode;
        length = 1;
    }*/

    // Linked List Destructor
    ~LinkedList() {
        Node *temp = head;
        while (head != nullptr) {
            head = head->next;
            delete temp;
            temp = head;
        }
    }

    // Printing all items in the LL
    void printList() {
        Node *temp = head;
        if (length == 0)
            cout << "The list is empty";
        while (temp->next) {
            cout << temp->redid << endl;
            temp = temp->next;
        }
    }

    // What's the first elemnt in the list?
    void getHead() {
        if (head == nullptr) {
            cout << "Head: nullptr" << endl;

        } else {
            cout << "Head: " << head->redid << ", " << head->first << head->last << endl;
        }
    }

    // What's the last element in the LL?
    void getTail() {
        if (tail == nullptr) {
            cout << "Tail: nullptr" << endl;
        } else {
            cout << "Tail: " << tail->redid << ", " << tail->first << tail-> last << endl;
        }
    }

    // How Long is the List?
    void getLength() { cout << "Length: " << length << endl; }

    // Get the elemt at a particular index
    Node *get(int index) {
        if (index < 0 || index >= length)
            return nullptr;
        Node *temp = head;
        for (int i = 0; i < index; ++i) {
            temp = temp->next;
        }
        return temp;
    }

    // set value at a particular index
    bool set(int index, int value, string first, string last) {
        Node *temp = get(index);
        if (temp != nullptr) {
            temp->redid = value;
            temp->first = first;
            temp->last = last;
            return true;
        }
        return false;
    }

    // Add node to the end of the list
    void append(int value, string first, string last) {
        Node *newNode = new Node(value, first, last, nullptr);
        if (length == 0) {
            head = newNode;
            tail = newNode;
        } else {
            tail->next = newNode;
            tail = newNode;
        }
        length++;
    }

    // Add a new node to the start of the list
    void prepend(int value, string first, string last) {
        Node *newNode = new Node(value, first, last, nullptr);
        if (length == 0) {
            head = newNode;
            tail = newNode;
        } else {
            newNode->next = head;
            head = newNode;
        }
        length++;
    }

    // Insert element at a particular index
    bool insert(int index, int value, string first, string last) {
        if (index < 0 || index > length)
            return false;
        if (index == 0) {
            prepend(value, first, last);
            return true;
        }
        if (index == length) {
            append(value, first, last);
            return true;
        }
        Node *newNode = new Node(value, first, last, nullptr);
        Node *temp = get(index - 1);
        newNode->next = temp->next;
        temp->next = newNode;
        length++;
        return true;
    }

    // Delete the first node in the list
    void deleteFirst() {
        if (length == 0)
            return;
        Node *temp = head;
        if (length == 1) {
            head = nullptr;
            tail = nullptr;
        } else {
            head = head->next;
        }
        delete temp;
        length--;
    }

    // Delete the last element of the list.
    void deleteLast() {
        if (length == 0)
            return;
        Node *temp = head;
        if (length == 1) {
            head = nullptr;
            tail = nullptr;
        } else {
            Node *pre = head;
            while (temp->next) {
                pre = temp;
                temp = temp->next;
            }
            tail = pre;
            tail->next = nullptr;
        }
        delete temp;
        length--;
    }

    // Delete a node at a particular index
    void deleteNode(int index) {
        if (index < 0 || index >= length)
            return;
        if (index == 0)
            return deleteFirst();
        if (index == length - 1)
            return deleteLast();

        Node *prev = get(index - 1);
        Node *temp = prev->next;

        prev->next = temp->next;
        delete temp;
        length--;
    }

    Node* getHeadNode() const { return head;}
    int getlengthInt() const { return length;}
    void selectionSortString() {
        Node *curr = head;

        while (curr != nullptr) {
            Node *minNode = curr;
            Node *comp = curr->next;
            while (comp != nullptr) {
                // compare data of first node with data present in each subsequent node
                if (comp->first < minNode->first) {
                    minNode = comp;
                }
                comp = comp->next;
            }
            // swap data of current node with minimum data node
            int temp = curr->redid;
            string tempName = curr->first;
            string tempLast = curr->last;

            curr->redid = minNode->redid;
            curr->first = minNode->first;
            curr->last = minNode->last;

            minNode->redid = temp;
            minNode->first = tempName;
            minNode->last = tempLast;

            // move current node pointer to next node
            curr = curr->next;
        }
    }
    void selectionSort() {
        Node *curr = head;

        while (curr != nullptr) {
            Node *minNode = curr;
            Node *comp = curr->next;
            while (comp != nullptr) {
                // compare data of first node with data present in each subsequent node
                if (comp->redid < minNode->redid) {
                    minNode = comp;
                }
                comp = comp->next;
            }
            // swap data of current node with minimum data node
            int temp = curr->redid;
            string tempName = curr->first;
            string tempLast = curr->last;

            curr->redid = minNode->redid;
            curr->first = minNode->first;
            curr->last = minNode->last;

            minNode->redid = temp;
            minNode->first = tempName;
            minNode->last = tempLast;
            // move current node pointer to next node
            curr = curr->next;
        }
    }
    void reverseList(){
        Node* prev = nullptr;
        Node* curr = head;
        Node* next = nullptr;

        while(curr!= nullptr){
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        head = prev;

    }
    void printLinkedList() {
        Node* current = head;
        if(length == 0)
            cout << "The list is empty";
        while (current != nullptr) {
            cout << current->redid << " "<< current->first << " " << current->last<< endl;
            current = current->next;
        }

    }



};


// main function
int main() {
    int choice;
    int length;
    int id;
    int index;
    int L;
    bool firstCalled = false;
    string first;
    string last;
    LinkedList* list;


    do{
        cout << "Choose from the following options:" << endl;
        cout << "1. Make a Linked List" << endl;
        cout << "2. Add a Node to the beginning" << endl;
        cout << "3. Add a Node to the End" << endl;
        cout << "4. Add a Node at Index" << endl;
        cout << "5. Delete Node from the beginning" << endl;
        cout << "6. Delete Node from the End" << endl;
        cout << "7. Delete Node at Index" << endl;
        cout << "8. Sort by Name" << endl;
        cout << "9. Sort by REDID" << endl;
        cout << "10. Reverse LinkedList" << endl;
        cout << "11. Exit" << endl;
        cout << "Enter Choice: " << endl;
        cin >> choice;

        switch(choice){
            case 1:
                //making linked list
                list = new LinkedList();
                cout << "Enter how many nodes:" ;
                cin >> length;
                for(int i=0; i < length; i++){
                    cout << "Enter the RedID " << i + 1 <<": ";
                    cin >> id;
                    std::cout << "Enter the First name " << i + 1 <<": ";
                    std::cin >> first;
                    std::cout << "Enter the Last name " << i + 1 <<": ";
                    std::cin >> last;
                    list->append(id,first,last);
                }
                cout << "Link List was created!" << endl;
                list->printLinkedList();
                firstCalled = true;
                break;
            case 2:
                if(!firstCalled){
                    cout << "Please make a Linked List" << endl;
                }
                else{
                    //Insert node at beginning
                    cout << "Enter RedID: ";
                    cin >> id;
                    std::cout << "Enter the First name : ";
                    std::cin >> first;
                    std::cout << "Enter the Last name: ";
                    std::cin >> last;
                    list->prepend(id,first,last);
                    list->printLinkedList();}
                break;
            case 3:
                if(!firstCalled){
                    cout << "Please make a Linked List" << endl;
                }
                else{
                    //Insert node at the end
                    L = list->getlengthInt();
                    cout << "Enter RedID: ";
                    cin >> id;
                    std::cout << "Enter the First name: ";
                    std::cin >> first;
                    std::cout << "Enter the Last name: ";
                    std::cin >> last;
                    list->append(id,first,last);
                    list->printLinkedList();}
                break;
            case 4:
                if(!firstCalled){
                    cout << "Please make a Linked List" << endl;
                }
                else{
                    //Insert at index
                    cout << "Enter RedID: ";
                    cin >> id;
                    std::cout << "Enter the First name: ";
                    std::cin >> first;
                    std::cout << "Enter the Last name: ";
                    std::cin >> last;
                    cout << "Enter the index: ";
                    cin >> index;

                    list->insert(index,id,first,last);

                    if(index > list->getlengthInt()){
                        cout << "Index exceeds length.\n"<<endl;
                    }
                    else{
                        cout << "Node " << index << " was inserted.\n"<< endl;
                    }
                    list->printLinkedList();}
                break;
            case 5:

                if(!firstCalled){
                    cout << "Please make a Linked List" << endl;
                }
                else {
                    //deletes head
                    L= list->getlengthInt();
                    if(L < 0){
                        cout << "You can't delete from an empty list." << endl;
                    } else {
                        list->deleteFirst();
                        cout << "Node was deleted" << endl;
                    }
                    list->printLinkedList();
                }
                break;
            case 6:
                if(!firstCalled){
                    cout << "Please make a Linked List" << endl;
                }
                else{
                    //deletes tail
                    L= list->getlengthInt();
                    if(L < 0){
                        cout << "You can't delete from an empty list." << endl;
                    }else{
                        list->deleteLast();
                        cout << "Node was deleted"<< endl;
                        list->printLinkedList();
                    }
                }
                break;
            case 7:
                if(!firstCalled){
                    cout << "Please make a Linked List" << endl;
                }
                else{
                    //deletes node at index
                    L = list->getlengthInt();
                    if(L < 0){
                        cout << "You can't delete from an empty list." << endl;
                    }else {
                        cout << "Enter the index: ";
                        cin >> index;
                        list->deleteNode(index);
                        if (index > L - 1) {
                            cout << "Index exceeds length.\n" << endl;
                        } else {
                            cout << "Node " << index << " was removed.\n" << endl;
                        }
                    }
                    list->printLinkedList();}
                break;
            case 8:
                if(!firstCalled){
                    cout << "Please make a Linked List" << endl;
                }
                else{
                    L= list->getlengthInt();
                    if(L > 0){
                        //Sorting method for a String
                        list->selectionSortString();
                        list->printLinkedList();}
                    else{
                        cout<< "You can't sort an empty list"<<endl;}
                }
                break;
            case 9:
                if(!firstCalled){
                    cout << "Please make a Linked List" << endl;
                }
                else{
                    L= list->getlengthInt();
                    if(L > 0){
                        //sorting method for RedID
                        list->selectionSort();
                        list->printLinkedList();}
                    else{
                        cout<< "You can't sort an empty list"<<endl;}
                }
                break;
            case 10:
                if(!firstCalled){
                    cout << "Please make a Linked List" << endl;
                }
                else {
                    L= list->getlengthInt();
                    if(L > 0){
                        //reverse link list needed to be created
                        list->reverseList();
                        list->printLinkedList();
                    }
                    else{
                        cout<< "You can't reverse an empty list"<<endl;}
                }
                break;
            case 11:
                //exiting the program
                cout << "Exiting... " << endl;

                break;
            case 12:
                // testing the output
                list->printLinkedList();
                break;
            default:
                cout << "Invalid, Please try again."<< endl;
                break;
        }
    }while(choice != 11);
    list->~LinkedList();
    return 0;
}

