import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export function SuperUserPanel() {
  return (
    <div className="flex flex-col gap-6">
      <Card>
        <CardHeader>
          <CardTitle>Super User Panel</CardTitle>
        </CardHeader>
        <CardContent>
          <p>Welcome to the super user panel.</p>
        </CardContent>
      </Card>
    </div>
  )
}
