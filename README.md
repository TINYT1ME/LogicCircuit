
<h1 align="center"  style="font-family: Courier, serif;">
  <a href="https://github.com/TINYT1ME/LogicCircuit/"><img src="https://i.postimg.cc/Gp3Cj8vM/logo.png" width="40" title="LogicCircuit"></a>
  Logic Circuit
</h1>

**LogicCircuit** is a lightweight application designed to help users build and simulate simple circuits using logic gates. This tool is perfect for beginners and educators who want to explore or teach the basics of how logic gates work.
![platforms](https://img.shields.io/badge/platforms-Windows%20%7C%20Mac%20%7C%20Linux-%23808080--%2332cd32)


----------

## 📃 Table of Contents

-   [Example](#-example)
-   [Installation](#-installation)
-   [How To Use](#-how-to-use)
    -   [Creating Components](#creating-components)
    -   [Deleting Components](#deleting-components)
    -   [Modifying Components](#modifying-components)
    -   [Working with Wires](#working-with-wires)
-   [License](#%EF%B8%8F-license)

----------

## 🟢 Example
<a href="https://github.com/TINYT1ME/LogicCircuit/"><img src="https://s9.gifyu.com/images/SFa8s.gif"  title="Example"></a>
----------

## 📦 Installation

1.  Clone the repository:
    
    ```bash
    git clone https://github.com/TINYT1ME/LogicCircuit
    ```
    
2.  Navigate to the project folder:
    
    ```bash
    cd LogicCircuit
    ```
    
3.  Install dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```
    
4.  Run the application:
    
    ```bash
    python logiccircuit/
    ```
    

----------

## ❓ How To Use

### Creating Components

-   **Logic Gates**: Select the desired logic gate type from the options at the bottom of the screen. Left-click anywhere on the canvas to place it.
-   **Switches**: Click the green "+Switch" button, then left-click on the canvas to place it.
-   **LEDs**: Click the green "+LED" button, then left-click on the canvas to place it.
-   **Wires**:
    1.  Left-click on the output square of a gate.
    2.  Move the mouse to create wire bends, clicking at each bend point.
    3.  Connect the wire by left-clicking on the input square of another gate or LED.

### Deleting Components

-   **Logic Gates**: Right-click on the gate to delete it.
-   **Switches**: Click the red "-Switch" button, then select the switch you want to remove.
-   **LEDs**: Click the red "-LED" button, then select the LED you want to remove.
-   **Wires**: Wires are automatically deleted when the connected gate, switch, or LED is removed.

### Modifying Components

-   **Switches**: Right-click on a switch to toggle its state.
-   **Logic Gates and LEDs**: These components are static and cannot be modified once placed.

### Working with Wires

-   **Creating Bends**: To adjust wire paths, click at desired points on the canvas while drawing a wire.
-   **Connecting Wires**: Ensure wires are connected to the correct input and output squares for proper circuit functionality.

----------

### ⚖️ License

MIT

----------
