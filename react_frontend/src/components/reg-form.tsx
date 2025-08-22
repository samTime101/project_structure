"use client"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { useState } from "react"
// Make sure this path is correct for your project structure
import { registerUser } from "@/services/reg-service" 
// Import the error type we defined in the service file
import type { DrfValidationError } from "@/services/reg-service"

// Define the type for the component's props for better type safety
interface RegFormProps extends React.ComponentProps<"div"> {
  onToggleForm: () => void;
}

export function RegForm({
  className,
  onToggleForm,
  ...props
}: RegFormProps) {
  const [email, setEmail] = useState("")
  const [phoneNumber, setPhoneNumber] = useState("")
  const [password, setPassword] = useState("")
  const [confirmPassword, setConfirmPassword] = useState("")
  const [username, setUsername] = useState("")

  // State for client-side and server-side validation errors
  const [emailError, setEmailError] = useState("")
  const [phoneNumberError, setPhoneNumberError] = useState("")
  const [passwordError, setPasswordError] = useState("")
  const [confirmPasswordError, setConfirmPasswordError] = useState("")
  const [usernameError, setUsernameError] = useState("")
  
  // State for generic errors (network issues, 500 errors, etc.)
  const [apiError, setApiError] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  

  // --- EVENT HANDLERS (Now with TypeScript event types) ---

  const handleEmailChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newEmail = e.target.value;
    setEmail(newEmail);
  }

  const handlePhoneNumberChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const number = e.target.value;
    setPhoneNumber(number);
  }

  const handlePasswordChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newPassword = e.target.value;
    setPassword(newPassword);
    // Also re-validate confirm password if password changes
    if (confirmPassword && newPassword !== confirmPassword) {
      setConfirmPasswordError("Passwords do not match.");
    } else {
      setConfirmPasswordError("");
    }
  }

  const handleConfirmPasswordChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const newConfirmPassword = e.target.value;
    setConfirmPassword(newConfirmPassword);
    if (password !== newConfirmPassword) {
      setConfirmPasswordError("Passwords do not match.");
    } else {
      setConfirmPasswordError("");
    }
  }

  

  const handleUsernameChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setUsername(e.target.value);
  };
  
  // --- FORM SUBMISSION HANDLER (The Core Logic) ---

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    // 1. Clear previous server-side errors
    setApiError("");
    setEmailError(prev => prev.includes("(from server)") ? "" : prev);
    setPhoneNumberError(prev => prev.includes("(from server)") ? "" : prev);
    setPasswordError(prev => prev.includes("(from server)") ? "" : prev);
    // setFirstnameError("");
    // setLastnameError("");
    setUsernameError("");
    
    // 2. Prevent submission if client-side validation fails
    if (isFormInvalid) {
        return;
    }

    setIsLoading(true);

    try {
      // 3. Call the API service
      const result = await registerUser({
        email,
        phoneNumber,
        password,
        username,
      });

      console.log("Registration successful:", result.message);
      // ===> SUCCESS! <===
      // You can now handle the successful registration. For example:
      // - Show a success message
      // - Redirect the user: router.push('/login')
      // - Toggle to the login form: onToggleForm()

    } catch (error) {
      // 4. Handle errors from the API service
      if (error instanceof Error) {
        // This handles generic errors (network, 500 status, etc.)
        setApiError(error.message);
      } else {
        // This handles the specific DRF validation error object
        const validationErrors = error as DrfValidationError;
        console.error("Validation errors:", validationErrors);

        // Iterate over the error object and set state for each field
        Object.keys(validationErrors).forEach((field) => {
          const message = `${validationErrors[field][0]} (from server)`;
          if (field === 'email') {
            setEmailError(message);
          } else if (field === 'phonenumber') { // Matches the DRF field name
            setPhoneNumberError(message);
          } else if (field === 'password') {
            setPasswordError(message);
          } else if (field === 'username') {
            setUsernameError(message);
          } else {
            // Catches 'non_field_errors' or other general errors from DRF
            setApiError(message);
          }
        });
      }
    } finally {
      // 5. Always stop the loading indicator
      setIsLoading(false);
    }
  };

  const isFormInvalid = !email || !phoneNumber || !password || !confirmPassword || !username || !!emailError || !!phoneNumberError || !!passwordError || !!confirmPasswordError;

  return (
    <div className={cn("flex flex-col gap-6", className)} {...props}>
      <Card>
        <CardHeader>
          <CardTitle>Create an account</CardTitle>
          <CardDescription>
            Enter your details below to create your account
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit}>
            <div className="flex flex-col gap-6">
            

              <div className="grid gap-3">
                <Label htmlFor="username">Username</Label>
                <Input id="username" type="text" value={username} onChange={handleUsernameChange} />
                {usernameError && <p className="text-red-500 text-sm">{usernameError}</p>}
              </div>
              {/* Email Input */}
              <div className="grid gap-3">
                <Label htmlFor="email">Email</Label>
                <Input id="email" type="email" value={email} onChange={handleEmailChange} />
                {emailError && <p className="text-red-500 text-sm">{emailError}</p>}
              </div>

              {/* Phone Number Input */}
              <div className="grid gap-3">
                <Label htmlFor="number">Phone Number</Label>
                <Input id="number" type="tel" value={phoneNumber} onChange={handlePhoneNumberChange} />
                {phoneNumberError && <p className="text-red-500 text-sm">{phoneNumberError}</p>}
              </div>

              {/* Password Input */}
              <div className="grid gap-3">
                <Label htmlFor="password">Password</Label>
                <Input id="password" type="password" value={password} onChange={handlePasswordChange} />
                {passwordError && <p className="text-red-500 text-sm">{passwordError}</p>}
              </div>

              {/* Confirm Password Input */}
              <div className="grid gap-3">
                <Label htmlFor="confirm-password">Repeat the Password</Label>
                <Input id="confirm-password" type="password" value={confirmPassword} onChange={handleConfirmPasswordChange} />
                {confirmPasswordError && <p className="text-red-500 text-sm">{confirmPasswordError}</p>}
              </div>
              
              {/* Display for generic API errors */}
              {apiError && <p className="text-red-500 text-sm text-center">{apiError}</p>}

              {/* Submit Button */}
              <div className="flex flex-col gap-3">
                <Button type="submit" className="w-full" disabled={isFormInvalid || isLoading}>
                  {isLoading ? 'Signing Up...' : 'Sign Up'}
                </Button>
              </div>
            </div>

            <div className="mt-4 text-center text-sm">
              Already have an account?{" "}
              <button type="button" onClick={onToggleForm} className="underline underline-offset-4">
                Log In
              </button>
            </div>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}