# Bitwise Operations

Bitwise operations are operations that are performed on the individual bits of a binary number. In other words, these operations work on the binary representation of a number, rather than its decimal or hexadecimal representation. Common bitwise operations include AND, OR, NOT, XOR, and bit shifting. These operations are performed on one or two operands, and the result of the operation is a new binary number.

## Pre-concepts

## Least Significant and Most Significant bits

The least significant bit (LSB) and the most significant bit (MSB) are terms used to describe the position of a bit within a binary number.

The least significant bit (LSB) is the bit that is located at the rightmost position in a binary number. It represents the lowest value in the number. The value of the least significant bit is $2^0$, which is 1, and it's the rightmost bit of a number, it's the least significant bit since it has the least impact on the overall value of the number. It's the bit that carries the least amount of weight in terms of numerical value. For example, in the binary number <code>1101</code>, the least significant bit is the rightmost bit, which is 1. This bit represents the value of $2^0$, or 1.

On the other hand, the most significant bit (MSB) is the bit that is located at the leftmost position in a binary number. It represents the highest value in the number. The value of the most significant bit is $2^{n-1}$, where n is the total number of bits in the number. It's the bit that carries the most amount of weight in terms of numerical value. For example, in the binary number <code>1101</code>, the most significant bit is the leftmost bit, which is 1. This bit represents the value of $2^3$, or 8.

These two concepts are relative and depend on the way the number is represented, in some systems a number can be represented in little-endian format, which means that the least significant byte is stored at the lowest memory address and the least significant bit is the rightmost bit, and in other systems, it can be represented in big-endian format, which means that the most significant byte is stored at the lowest memory address and the most significant bit is the leftmost bit. On the other hand, the MSB is often used to determine the sign of a number in a computer system, if the MSB is 1, the number is considered negative, and if the MSB is 0, the number is considered positive. It is also used to check for overflow when performing arithmetic operations.

Additionally, the LSB and MSB are also important in computer memory and storage systems. In digital signal processing, for example, the LSB is sometimes used as a measure of the signal-to-noise ratio (SNR) or quantization noise. And in data compression, the MSB is often used to represent the most important data and the LSB to represent the least important data.

In summary, LSB and MSB are important concepts in digital systems, and they are used to represent and manipulate data at the bit level. The LSB is the rightmost bit in a binary number and represents the least significant part of the number. The LSB is the bit that carries the least weight in terms of numerical value and is often the first bit affected by bitwise operations.
The MSB is the leftmost bit in a binary number and represents the most significant part of the number. The MSB carries the most weight in terms of numerical value and is often used to check for overflow or to determine the sign of a number. Understanding these concepts can help in improving the efficiency, performance, and accuracy of digital systems, as well as in understanding the behavior of the system such as data compression and digital signal processing.

In summary, understanding the LSB and MSB can help you in improving the efficiency, performance, and accuracy of digital systems, by allowing you to manipulate data at the bit level. They are important concepts in digital signal processing, data compression, and other fields where bit-level manipulation is required.

In addition to the examples above, LSB and MSB are also used in image processing and computer vision, where the LSBs of the pixel values can be used to hide or encrypt data, while the MSBs can be used to store important visual information. Also, in cryptography, the LSBs can be used to hide the secret data in an image while the MSBs can be used to store the original image.

In computer networks, LSB and MSB are used to encode the IP address, where the MSBs are used to specify the network address and the LSBs are used to specify the host address.

In conclusion, LSB and MSB are important concepts that are widely used in digital systems, and understanding their properties and behavior can help in improving the efficiency, performance, and accuracy of digital systems.

## Bitwise operation types

1. **AND (&)**: This operator compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1, otherwise, it's set to 0.

```
x = 12 # 1100 in binary
y = 5  # 0101 in binary
result = x & y # 0100 = 4

```

2. **OR (|)**: This operator compares each bit of the first operand to the corresponding bit of the second operand. If either bit is 1, the corresponding result bit is set to 1, otherwise, it's set to 0.

```
x = 12 # 1100 in binary
y = 5  # 0101 in binary
result = x | y # <code>1101</code> = 13


```

3. **XOR (^)**: This operator compares each bit of the first operand to the corresponding bit of the second operand. If both bits are the same, the corresponding result bit is set to 0, otherwise, it's set to 1.

```
x = 12 # 1100 in binary
y = 5  # 0101 in binary
result = x ^ y # 1001 = 9

```

4. **NOT (~)**: This operator inverts all the bits of the operand.

```
x = 12 # 1100 in binary
result = ~x # -13 in decimal, two's complement of 12

```

5. **Bitwise Left Shift (<<)**: This operation shifts the bits of the first operand to the left by the number of positions specified in the second operand, and fills in the empty rightmost bits with 0s. For example:

```
x = 12 # 1100 in binary
result = x << 2 # 48 = 0011 0000

```

In this example, we are shifting the bits of x to the left by 2 places, which results in the number 48.

6. **Bitwise Right Shift (>>)**: This operation shifts the bits of the first operand to the right by the number of positions specified in the second operand, and fills in the empty leftmost bits with 0s or 1s depending on the sign bit. for example:

```
x = 12 # 1100 in binary
result = x >> 2 # 3 = 0000 0011

```

In this example, we are shifting the bits of x to the right by 2 places, which results in the number 3.

Note that the bitwise shift operations are used to quickly multiply or divide an integer by a power of 2.

You can use bitwise operation on any integer type in python, including signed and unsigned integers, and long integers.

---

## Benefits of bitwise operations include:

- Efficiency: Bitwise operations are typically faster than equivalent arithmetic operations because they are performed at the level of individual bits rather than entire numbers.

- Compactness: Bitwise operations can be used to perform multiple operations at once, and therefore they can reduce the number of instructions required to accomplish a task.

- Memory savings: Bitwise operations can be used to manipulate flags, which can save memory by representing multiple Boolean values using a single byte, rather than one byte per value.

- Low-level control: Bitwise operations can be used to directly manipulate memory at the bit level, which can be useful for low-level programming tasks such as device drivers and embedded systems.

- Cryptography: Bitwise operations are used in cryptography and security to create and decrypt secure messages, for example in block ciphers like AES.

It's worth noting that, bitwise operations are not only used in low-level programming, but also in high-level programming in some specific scenarios, such as compression, image processing, and data storage and retrieval.

## Examples:

1. Efficiency:

   Bitwise operations can be faster than arithmetic operations for certain tasks. For example, checking if a number is even or odd can be done with a bitwise AND operation. Here's how it works: The AND operation compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1, otherwise, it's set to 0. When we perform the AND operation between an integer and 1, if the least significant bit of the integer is 1, the result will be 1, which means the number is odd, otherwise, the result will be 0, which means the number is even.

   ```
   bool is_even(int x) {
       return (x & 1) == 0;
   }

   ```

   This is faster than using the modulo operator (%), which is the equivalent arithmetic operation.

   ```
   bool is_even(int x) {
       return x % 2 == 0;
   }
   ```

2. Compactness:

   Bitwise operations can be used to perform multiple operations at once. For example, the following C++ code uses bitwise operations to set and clear certain bits in a number, without affecting the other bits. To set a bit we use the OR operation, which sets a bit to 1 if either operand's bit is 1. To clear a bit we use the AND operation with NOT operator, which sets a bit to 0 if either operand's bit is 0.

   ```
   unsigned int flags = 0;
   // Set the first and third bits
   flags = flags | (1 << 0) | (1 << 2);
   // Clear the second bit
   flags = flags & ~(1 << 1);

   ```

3. Memory savings:

   Bitwise operations can be used to manipulate flags, which can save memory by representing multiple Boolean values using a single byte. For example, the following C++ code uses a single byte to represent the state of four Boolean flags. To set a flag we use the OR operation and to check the value of a flag we use the AND operation.

   ```
   unsigned char flags = 0;
   // Set flag 0
   flags = flags | (1 << 0);
   // Check if flag 2 is set
   if (flags & (1 << 2)) {
    // Do something
   }

   ```

4. Low-level control:

   Bitwise operations can be used to directly manipulate memory at the bit level. For example, the following C++ code uses bitwise operations to change the order of the bits in a number. In this example, we use a loop to iterate through all the bits of the number, and for each bit, we shift it to the position that is equal to the total number of bits minus the current position of the bit minus 1, and we use OR operation to combine the bits in the correct order.

   ```
   unsigned int x = 0b10101010;
   unsigned int y = 0;
   // Reverse the order of the bits in x
   for (int i = 0; i < sizeof(x) * 8; i++) {
    y |= ((x >> i) & 1) << (sizeof(x) * 8 - i - 1);
   }


   ```

   Python

   ```
   x = int("10101010", 2)
   y = 0

   # Reverse the order of the bits in x

   for i in range(8):
   y |= (x >> i & 1) << (8 - i - 1)

   ```

   In this code snippet, we first initialize the variable x with the binary value 10101010 using the int() function with a base of 2. Then we initialize the variable y with the value 0.

   We use a for loop, and the range function to iterate 8 times, which is the number of bits we want to reverse. In each iteration, we use bitwise operator >> and & to get the value of each bit in x, and then we use << operator to shift the bit to its new position, and finally we use the bitwise OR operator |= to combine all the reversed bits together to get the final result in the variable y.

   It's worth noting that, in Python, the built-in function bin() returns a string, so if you want to use a binary value as a number, you need to use the int() function with a base of 2. Also, python uses 0-based indexing, so we don't need to multiply the size of x by 8, and we can use 8 directly as the range of the loop.

5. Cryptography: Bitwise operations are used in cryptography and security to create and decrypt secure messages. For example, the Advanced Encryption Standard (AES) is a block cipher that uses bitwise operations such
